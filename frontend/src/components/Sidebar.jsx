import React from 'react';

function Sidebar({ conversations, activeConversationId, onSelectConversation, onNewChat, onDeleteConversation }) {
  const handleDeleteClick = (e, conversationId) => {
    e.stopPropagation(); // Prevent conversation selection when clicking delete
    if (window.confirm('Are you sure you want to delete this conversation?')) {
      onDeleteConversation(conversationId);
    }
  };

  return (
    <div className="sidebar">
      {/* Conversations List - Horizontal Scroll */}
      {conversations.map((conv) => (
        <div
          key={conv.id}
          className={`relative group sidebar-item ${
            activeConversationId === conv.id ? 'active' : ''
          }`}
          onClick={() => onSelectConversation(conv.id)}
          title={conv.title || 'New Conversation'}
        >
          <svg xmlns="http://www.w3.org/2000/svg" className="h-3.5 w-3.5 flex-shrink-0" viewBox="0 0 20 20" fill="currentColor">
            <path fillRule="evenodd" d="M18 10c0 3.866-3.582 7-8 7a8.841 8.841 0 01-4.083-.98L2 17l1.338-3.123C2.493 12.767 2 11.434 2 10c0-3.866 3.582-7 8-7s8 3.134 8 7zM7 9H5v2h2V9zm8 0h-2v2h2V9zM9 9h2v2H9V9z" clipRule="evenodd" />
          </svg>
          <span className="truncate">{conv.title || 'New'}</span>

          {/* Delete Button */}
          <button
            onClick={(e) => handleDeleteClick(e, conv.id)}
            className="opacity-0 group-hover:opacity-100 transition-opacity p-0.5 rounded hover:bg-red-500/20 text-red-400"
            title="Delete"
          >
            <svg xmlns="http://www.w3.org/2000/svg" className="h-3 w-3" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>
        </div>
      ))}
    </div>
  );
}

export default Sidebar; 