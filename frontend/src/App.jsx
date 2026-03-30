import { useState, useRef, useEffect } from 'react'
import './App.css'
import { convertCode, getConversationContext } from './services/api'
import Sidebar from './components/Sidebar'
import ThemeToggle from './components/ThemeToggle'
import {
  loadConversations,
  saveConversations,
  createConversation,
  addMessageToConversation,
  deleteConversation,
  getConversation,
  updateConversationContext
} from './services/conversationService'

function App() {
  const [conversations, setConversations] = useState(() => loadConversations())
  const [activeConversationId, setActiveConversationId] = useState(null)
  const [inputMessage, setInputMessage] = useState('')
  const [isLoading, setIsLoading] = useState(false)
  const chatEndRef = useRef(null)
  const inputRef = useRef(null)

  // Initialize with a new conversation if none exists
  useEffect(() => {
    if (conversations.length === 0) {
      const newConversation = createConversation()
      setConversations([newConversation])
      setActiveConversationId(newConversation.id)
    } else if (!activeConversationId) {
      setActiveConversationId(conversations[0].id)
    }
  }, [])

  // Save conversations to localStorage whenever they change
  useEffect(() => {
    saveConversations(conversations)
  }, [conversations])

  // Scroll to bottom when messages change
  useEffect(() => {
    chatEndRef.current?.scrollIntoView({ behavior: 'smooth' })
  }, [conversations, activeConversationId])

  // Load conversation context when switching conversations
  useEffect(() => {
    if (activeConversationId) {
      loadConversationContext(activeConversationId)
      // Auto-focus input when switching conversations
      setTimeout(() => {
        inputRef.current?.focus()
        adjustTextareaHeight()
      }, 100)
    }
  }, [activeConversationId])

  // Auto-focus input on initial load
  useEffect(() => {
    setTimeout(() => {
      inputRef.current?.focus()
      adjustTextareaHeight()
    }, 200)
  }, [])

  // Adjust height on initial render and when inputMessage changes
  useEffect(() => {
    adjustTextareaHeight()
  }, [inputMessage])

  // Adjust height on window resize
  useEffect(() => {
    const handleResize = () => adjustTextareaHeight()
    window.addEventListener('resize', handleResize)
    return () => window.removeEventListener('resize', handleResize)
  }, [])

  // Function to adjust textarea height
  const adjustTextareaHeight = () => {
    const textarea = inputRef.current
    if (textarea) {
      // Reset height to auto to get the correct scrollHeight
      textarea.style.height = 'auto'
      
      // Calculate line height more accurately
      const computedStyle = window.getComputedStyle(textarea)
      const lineHeight = parseInt(computedStyle.lineHeight) || 24
      const paddingTop = parseInt(computedStyle.paddingTop) || 0
      const paddingBottom = parseInt(computedStyle.paddingBottom) || 0
      
      // Minimum height should match the send button (56px to match py-3 + content)
      const minHeight = 56
      // Maximum height for 5 lines
      const maxHeight = (lineHeight * 5) + paddingTop + paddingBottom
      
      // Calculate new height based on content, but respect min/max
      const contentHeight = textarea.scrollHeight
      const newHeight = Math.max(minHeight, Math.min(contentHeight, maxHeight))
      
      textarea.style.height = `${newHeight}px`
      
      // Enable/disable scrolling based on whether we're at max height
      if (contentHeight > maxHeight) {
        textarea.style.overflowY = 'auto'
      } else {
        textarea.style.overflowY = 'hidden'
      }
    }
  }

  // Update height when input changes
  const handleInputChange = (e) => {
    setInputMessage(e.target.value)
    adjustTextareaHeight()
  }

  const loadConversationContext = async (conversationId) => {
    try {
      const context = await getConversationContext(conversationId)
      if (context) {
        // Update the conversation with context info from backend
        setConversations(prev => prev.map(conv => 
          conv.id === conversationId 
            ? updateConversationContext(conv, {
                direction: context.direction,
                lastCode: context.last_code_preview || conv.lastCode
              })
            : conv
        ))
      }
    } catch (error) {
      console.error('Error loading conversation context:', error)
    }
  }

  const handleNewChat = () => {
    const newConversation = createConversation()
    setConversations(prev => [...prev, newConversation])
    setActiveConversationId(newConversation.id)
    setInputMessage('')
    // Auto-focus input for new chat
    setTimeout(() => {
      inputRef.current?.focus()
      adjustTextareaHeight()
    }, 100)
  }

  const handleSelectConversation = (conversationId) => {
    setActiveConversationId(conversationId)
    setInputMessage('')
  }

  const handleDeleteConversation = (conversationId) => {
    // Don't allow deleting the last conversation
    if (conversations.length <= 1) {
      alert('Cannot delete the last conversation. Create a new one first.')
      return
    }

    // Remove the conversation
    const updatedConversations = conversations.filter(conv => conv.id !== conversationId)
    setConversations(updatedConversations)

    // If we're deleting the active conversation, switch to another one
    if (activeConversationId === conversationId) {
      const remainingConversations = updatedConversations
      if (remainingConversations.length > 0) {
        setActiveConversationId(remainingConversations[0].id)
      }
    }
  }

  const activeConversation = getConversation(conversations, activeConversationId)
  const messages = activeConversation?.messages || []

  const handleSendMessage = async (e) => {
    e.preventDefault()
    if (!inputMessage.trim() || !activeConversationId) return

    const timestamp = new Date().toISOString()
    const tempId = Date.now()

    // Add user message
    const userMessage = {
      id: tempId,
      text: inputMessage,
      sender: 'user',
      timestamp,
      status: 'sent'
    }

    setConversations(prev => prev.map(conv => 
      conv.id === activeConversationId
        ? addMessageToConversation(conv, userMessage)
        : conv
    ))

    setInputMessage('')
    setIsLoading(true)

    try {
      // Call the API with conversation ID
      const response = await convertCode(inputMessage, activeConversationId)
      
      // Check for language mismatch error
      if (response.result && typeof response.result === 'object' && response.result.error) {
        if (response.result.type === 'language_mismatch') {
          // Show language mismatch as chat message instead of alert
          setConversations(prev => prev.map(conv => {
            if (conv.id === activeConversationId) {
              const updatedMessages = conv.messages.map(msg => 
                msg.id === tempId ? { ...msg, status: 'delivered' } : msg
              )
              
              const alertMessage = {
                id: tempId + 1,
                text: `⚠️ ${response.result.error}`,
                sender: 'bot',
                timestamp: new Date().toISOString(),
                isError: true,
                type: 'language_mismatch'
              }
              
              return {
                ...conv,
                messages: [...updatedMessages, alertMessage]
              }
            }
            return conv
          }))
          setIsLoading(false)
          return
        }
      }
      
      // Update the conversation with both messages
      setConversations(prev => prev.map(conv => {
        if (conv.id === activeConversationId) {
          // Update user message status and add bot response
          const updatedMessages = conv.messages.map(msg => 
            msg.id === tempId ? { ...msg, status: 'delivered' } : msg
          )
          
          const botMessage = {
          id: tempId + 1,
            text: formatBotResponse(response),
          sender: 'bot',
            timestamp: new Date().toISOString(),
            type: response.type
          }
          
          // Update conversation direction if included in response
          const updatedConv = {
            ...conv,
            messages: [...updatedMessages, botMessage]
          }
          
          if (response.direction) {
            updatedConv.direction = response.direction
          }
          
          return updatedConv
        }
        return conv
      }))
    } catch (error) {
      // Handle error
      setConversations(prev => prev.map(conv => {
        if (conv.id === activeConversationId) {
          const errorMessage = {
          id: tempId + 1,
          text: 'Error: Could not process your request. Please try again.',
          sender: 'bot',
          timestamp: new Date().toISOString(),
          isError: true
        }
          return addMessageToConversation(conv, errorMessage)
        }
        return conv
      }))
    } finally {
      setIsLoading(false)
      // Auto-focus input after sending message
      setTimeout(() => {
        inputRef.current?.focus()
        adjustTextareaHeight()
      }, 100)
    }
  }

  const formatBotResponse = (response) => {
    const { result, type, message } = response
    
    switch (type) {
      case 'converted_code':
        return message ? `${message}\n\n${result}` : result
      case 'grammar':
        return message ? `${message}\n\n${result}` : `Parse Tree:\n\n${result}`
      case 'output':
        return message ? `${message}\n\n${result}` : `Output:\n\n${result}`
      case 'message':
        return result
      case 'code':
        return message ? `${message}\n\n${result}` : `Saved Code:\n\n${result}`
      default:
        return result
    }
  }

  const handleKeyPress = (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault()
      handleSendMessage(e)
    }
  }

  return (
    <div className="chat-container flex h-screen w-screen">
      {/* Sidebar */}
      <Sidebar
        conversations={conversations}
        activeConversationId={activeConversationId}
        onSelectConversation={handleSelectConversation}
        onNewChat={handleNewChat}
        onDeleteConversation={handleDeleteConversation}
      />

      {/* Main Chat Area */}
      <div className="flex-1 flex flex-col w-[75%] max-w-full">
      {/* Header */}
        <header className="header-modern">
          <div className="flex items-center justify-between">
            <div>
              <h1 className="text-xl font-semibold">
                {activeConversation?.title || 'New Conversation'}
              </h1>
              {activeConversation?.lastCode && (
                <div className="text-sm text-muted mt-1">
                  Context: {activeConversation.direction === 'pytojava' ? 'Python → Java' : 'Java → Python'} 
                  {activeConversation.lastLanguage && ` (${activeConversation.lastLanguage})`}
                </div>
              )}
            </div>
            <div className="flex items-center gap-2 text-sm text-muted">
              <ThemeToggle />
              <div className="w-2 h-2 bg-green-500 rounded-full"></div>
              Online
            </div>
          </div>
      </header>

      {/* Chat Messages */}
        <div className="flex-1 overflow-y-auto p-6 space-y-6 smooth-scroll">
          {messages.length === 0 && (
            <div className="flex items-center justify-center h-full">
              <div className="text-center max-w-md">
                <div className="text-gradient text-2xl font-bold mb-4">
                  Welcome to Code Converter
                </div>
                <p className="text-muted mb-6">
                  Transform your code between Python and Java instantly. Each conversation remembers its own context.
                </p>
                <div className="grid grid-cols-2 gap-4 text-sm">
                  <div className="bg-secondary p-4 rounded-lg">
                    <div className="font-medium mb-2">🧠 Context Memory</div>
                    <div className="text-muted">Each conversation remembers its code</div>
                  </div>
                  <div className="bg-secondary p-4 rounded-lg">
                    <div className="font-medium mb-2">🚀 Smart Commands</div>
                    <div className="text-muted">Try "show grammar", "show output"</div>
                  </div>
                </div>
              </div>
            </div>
          )}

        {messages.map((message) => (
          <div
            key={message.id}
              className={`message-animate flex ${message.sender === 'user' ? 'justify-end' : 'justify-start'}`}
          >
            <div
                className={`${
                message.sender === 'user'
                    ? 'message-user'
                  : message.isError
                    ? 'message-bot message-error'
                    : 'message-bot'
                }`}
              >
                <div className="whitespace-pre-wrap font-mono text-sm leading-relaxed">
                  {message.text}
                </div>
                <div className={`mt-3 pt-3 border-t ${
                  message.sender === 'user' 
                    ? 'text-white/70 border-white/20 text-xs opacity-80' 
                    : 'text-timestamp border-gray-200/40'
                }`}>
                  {new Date(message.timestamp).toLocaleTimeString([], { 
                    hour: '2-digit', 
                    minute: '2-digit' 
                  })}
                {message.status && <span> · {message.status}</span>}
                  {message.type && <span> · {message.type}</span>}
                </div>
            </div>
          </div>
        ))}
        
        {/* Loading indicator */}
        {isLoading && (
          <div className="flex justify-start">
              <div className="message-bot">
                <div className="loading-dots">
                  <div className="loading-dot"></div>
                  <div className="loading-dot"></div>
                  <div className="loading-dot"></div>
                </div>
                <div className="text-muted text-sm mt-2">Processing with conversation context...</div>
            </div>
          </div>
        )}
        
        <div ref={chatEndRef} />
      </div>

      {/* Input Area */}
        <div className="p-6 border-divider border-t backdrop-blur">
          <form onSubmit={handleSendMessage} className="max-w-4xl mx-auto">
            <div className="flex gap-4 items-end">
          <textarea
            value={inputMessage}
                onChange={handleInputChange}
            onKeyDown={handleKeyPress}
                placeholder="Enter code or commands like 'show grammar', 'show output', 'translate python to java'..."
                className="input-modern flex-1 resize-none"
                disabled={isLoading}
                ref={inputRef}
                style={{ 
                  minHeight: '56px',
                  maxHeight: '140px', // 5 lines approx
                  height: '56px',
                  overflowY: 'hidden'
                }}
          />
          <button
            type="submit"
            disabled={isLoading || !inputMessage.trim()}
                className={`btn-primary px-6 py-3 h-14 ${
              inputMessage.trim() && !isLoading
                    ? 'glow-accent-hover'
                    : 'opacity-50 cursor-not-allowed'
            }`}
          >
            {isLoading ? (
                  <div className="loading-dots">
                    <div className="loading-dot bg-white"></div>
                    <div className="loading-dot bg-white"></div>
                    <div className="loading-dot bg-white"></div>
                  </div>
            ) : (
              <svg className="h-5 w-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M12 19l9 2-9-18-9 18 9-2zm0 0v-8"></path>
              </svg>
            )}
          </button>
        </div>
      </form>
        </div>
      </div>
    </div>
  )
}

export default App