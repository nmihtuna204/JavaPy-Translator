const STORAGE_KEY = 'code_converter_conversations';

// Load conversations from localStorage
export const loadConversations = () => {
  const stored = localStorage.getItem(STORAGE_KEY);
  if (!stored) return [];
  try {
    return JSON.parse(stored);
  } catch (e) {
    console.error('Failed to parse conversations:', e);
    return [];
  }
};

// Save conversations to localStorage
export const saveConversations = (conversations) => {
  localStorage.setItem(STORAGE_KEY, JSON.stringify(conversations));
};

// Create a new conversation
export const createConversation = () => {
  return {
    id: Date.now().toString(),
    title: 'New Conversation',
    messages: [],
    lastCode: null,
    lastLanguage: null,
    direction: 'pytojava',
    createdAt: new Date().toISOString(),
  };
};

// Detect if text contains code
export const isCodeInput = (text) => {
  const codePatterns = [
    // Variable assignments
    /\w+\s*=\s*.+/,
    // Function definitions
    /(def|function|class)\s+\w+/,
    // Control structures
    /(if|for|while|try|catch)\s*\(/,
    // Python specific
    /(import|from)\s+\w+/,
    // Java specific
    /(public|private|protected)\s+(class|interface|static)/,
    // Common programming constructs
    /[\{\}\[\];]/,
    // Method calls with parentheses
    /\w+\.\w+\(/,
    // Print statements
    /(print|console\.log|System\.out)/,
  ];
  
  return codePatterns.some(pattern => pattern.test(text.trim()));
};

// Detect if text is a command
export const isCommand = (text) => {
  const commandPatterns = [
    /show\s+grammar/i,
    /show\s+tree/i,
    /parse\s+tree/i,
    /syntax\s+tree/i,
    /show\s+output/i,
    /run\s+code/i,
    /execute/i,
    /save\s+code/i,
    /show\s+saved\s+code/i,
    /show\s+code/i,
    /convert\s+to\s+(python|java)/i,
    /translate\s+to\s+(python|java)/i,
    /java\s+to\s+python/i,
    /python\s+to\s+java/i,
    /switch\s+to\s+(python|java)/i,
    /analyze/i,
    /explain/i,
  ];
  
  return commandPatterns.some(pattern => pattern.test(text.trim()));
};

// Update conversation title based on first message
export const updateConversationTitle = (conversation) => {
  if (conversation.messages.length > 0) {
    const firstMessage = conversation.messages[0];
    // If it's code, use the first line or first 30 characters
    const title = firstMessage.text.split('\n')[0].substring(0, 30);
    return {
      ...conversation,
      title: title + (title.length === 30 ? '...' : ''),
    };
  }
  return conversation;
};

// Add message to conversation and update context
export const addMessageToConversation = (conversation, message) => {
  const updatedConversation = {
    ...conversation,
    messages: [...conversation.messages, message],
  };
  
  // If this is a user message with code, update the lastCode
  if (message.sender === 'user' && message.text.trim()) {
    const code = message.text.trim();
    // Simple heuristic to detect if it's code vs command
    if (!isCommand(code)) {
      updatedConversation.lastCode = code;
      updatedConversation.lastLanguage = detectLanguage(code);
    }
  }
  
  return updateConversationTitle(updatedConversation);
};

// Simple language detection
const detectLanguage = (code) => {
  // Basic heuristics for language detection
  if (code.includes('def ') || code.includes('print(') || code.includes('if __name__')) {
    return 'python';
  } else if (code.includes('public class') || code.includes('System.out.println') || code.includes('public static void main')) {
    return 'java';
  }
  return 'unknown';
};

// Delete a conversation
export const deleteConversation = (conversations, conversationId) => {
  return conversations.filter(conv => conv.id !== conversationId);
};

// Get a conversation by ID
export const getConversation = (conversations, conversationId) => {
  return conversations.find(conv => conv.id === conversationId);
};

// Update conversation context
export const updateConversationContext = (conversation, updates) => {
  return {
    ...conversation,
    ...updates
  };
}; 