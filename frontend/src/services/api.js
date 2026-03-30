const API_BASE_URL = 'http://localhost:8000';

// Map frontend commands to backend commands
const mapCommand = (command) => {
  const cmd = command.toLowerCase().trim();
  
  if (cmd.includes('grammar') || cmd.includes('tree')) {
    return 'showgrammar';
  }
  if (cmd.includes('output') || cmd.includes('run')) {
    return 'showoutput';
  }
  if (cmd.includes('save')) {
    return 'savecode';
  }
  if (cmd.includes('show') && cmd.includes('code')) {
    return 'showsavedcode';
  }
  if (cmd.includes('java') && cmd.includes('python')) {
    return 'javatopy';
  }
  if (cmd.includes('python') && cmd.includes('java')) {
    return 'pytojava';
  }
  
  return command; // Return original if no mapping found
};

export const convertCode = async (code, conversationId = null) => {
  try {
    const response = await fetch(`${API_BASE_URL}/convert`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ 
        code,
        conversation_id: conversationId 
      }),
    });

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    const data = await response.json();
    
    // Handle error responses from backend
    if (data.error) {
      return {
        result: {
          error: data.error,
          type: data.type || 'error'
        },
        type: 'error',
        message: data.message || 'An error occurred',
        conversationId: data.conversation_id || conversationId
      };
    }
    
    // Handle different response types with appropriate messages
    let responseMessage = data.message || '';
    
    // If no message is provided, generate a default based on type
    if (!responseMessage && data.type) {
      switch (data.type) {
        case 'converted_code':
          responseMessage = 'Code converted successfully!';
          break;
        case 'message':
          responseMessage = data.result || 'Operation completed';
          break;
        case 'code':
          responseMessage = 'Here is your saved code:';
          break;
        case 'grammar':
          responseMessage = 'Here is the parse tree for your code:';
          break;
        case 'output':
          responseMessage = data.message || 'Here is the output of your code:';
          break;
        default:
          responseMessage = 'Operation completed successfully';
      }
    }
    
    return {
      result: data.result || data.converted_code || 'Operation completed successfully',
      type: data.type || 'converted_code',
      message: responseMessage,
      conversationId: data.conversation_id,
      direction: data.direction
    };
  } catch (error) {
    console.error('Error converting code:', error);
    
    throw error;
  }
};

export const getConversationContext = async (conversationId) => {
  try {
    const response = await fetch(`${API_BASE_URL}/conversation/${conversationId}/context`);
    
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    
    return await response.json();
  } catch (error) {
    console.error('Error getting conversation context:', error);
    return null;
  }
}; 