import React from 'react';

function Sidebar({ conversations, activeConversationId, onSelectConversation, onNewChat, onDeleteConversation }) {
  const handleDeleteClick = (e, conversationId) => {
    e.stopPropagation(); // Prevent conversation selection when clicking delete
    if (window.confirm('Are you sure you want to delete this conversation?')) {
      onDeleteConversation(conversationId);
    }
  };

  return (
    <div className="sidebar w-[15%] min-w-[280px] h-screen flex flex-col">
      {/* Header */}
      <div className="p-6">
        <h2 className="text-gradient text-xl font-bold mb-6">Code Converter</h2>
        
        {/* New Chat Button */}
        <button
          onClick={onNewChat}
          className="sidebar-new-chat w-full glow-accent-hover"
        >
          <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
            <path fillRule="evenodd" d="M10 3a1 1 0 00-1 1v5H4a1 1 0 100 2h5v5a1 1 0 102 0v-5h5a1 1 0 100-2h-5V4a1 1 0 00-1-1z" clipRule="evenodd" />
          </svg>
          New Chat
        </button>
      </div>

      {/* Divider */}
      <div className="border-divider border-t mx-6 mb-4"></div>

      {/* Conversations List */}
      <div className="flex-1 overflow-y-auto px-3">
        <div className="space-y-1">
          {conversations.map((conv) => (
            <div
              key={conv.id}
              className={`relative group sidebar-item ${
                activeConversationId === conv.id ? 'active' : ''
              }`}
              onClick={() => onSelectConversation(conv.id)}
            >
              <div className="flex flex-col flex-1 text-left min-w-0 pr-8">
                <div className="flex items-center gap-2">
                  <svg xmlns="http://www.w3.org/2000/svg" className="h-4 w-4 flex-shrink-0" viewBox="0 0 20 20" fill="currentColor">
                    <path fillRule="evenodd" d="M18 10c0 3.866-3.582 7-8 7a8.841 8.841 0 01-4.083-.98L2 17l1.338-3.123C2.493 12.767 2 11.434 2 10c0-3.866 3.582-7 8-7s8 3.134 8 7zM7 9H5v2h2V9zm8 0h-2v2h2V9zM9 9h2v2H9V9z" clipRule="evenodd" />
                  </svg>
                  <div className="truncate flex-1">
                    {conv.title || 'New Conversation'}
                  </div>
                </div>
                
                {/* Context indicators */}
                {conv.lastCode && (
                  <div className="flex items-center gap-2 mt-1 text-xs opacity-60">
                    <div className="flex items-center gap-1">
                      <div className="w-2 h-2 bg-green-400 rounded-full"></div>
                      <span>
                        {conv.direction === 'pytojava' 
                          ? 'translate 🐍 to ☕' 
                          : 'translate ☕ to 🐍'}
                      </span>
                    </div>
                    {/* <div className="flex items-center gap-1">
                      <span>{conv.direction === 'pytojava' ? '🐍→☕' : '☕→🐍'}</span>
                    </div> */}
                    {conv.lastLanguage && (
                      <div className="bg-purple-500/20 px-2 py-0.5 rounded text-xs">
                        {conv.lastLanguage}
                      </div>
                    )}
                  </div>
                )}
              </div>
              
              {/* Delete Button */}
              <button
                onClick={(e) => handleDeleteClick(e, conv.id)}
                className="absolute top-1/2 right-2 transform -translate-y-1/2 opacity-0 group-hover:opacity-100 transition-all duration-200 p-1 rounded-md hover:bg-red-500/20 text-red-400 hover:text-red-300 z-10"
                title="Delete conversation"
              >
                <svg xmlns="http://www.w3.org/2000/svg" className="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1-1H8a1 1 0 00-1 1v3M4 7h16" />
                </svg>
              </button>
              
              {/* Active indicator - only show when not hovering */}
              {activeConversationId === conv.id && (
                <div className="absolute top-1/2 right-2 transform -translate-y-1/2 w-2 h-2 bg-gradient-to-r from-purple-500 to-purple-400 rounded-full flex-shrink-0 group-hover:opacity-0 transition-opacity duration-200"></div>
              )}
            </div>
          ))}
        </div>
      </div>

      {/* Footer */}
      <div className="p-6 border-divider border-t">
        <div className="text-xs text-muted text-center">
          Context-Aware Code Converter
        </div>
      </div>
    </div>
  );
}

export default Sidebar; 