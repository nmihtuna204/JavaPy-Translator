export const convertCode = async (code, conversationId) => {
  try {
    const res = await fetch('http://localhost:8000/convert', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        code: code.trim() + '\n',
        conversation_id: conversationId
      }),
    });
    const data = await res.json();

    // Handle error response
    if (data.error) {
      return {
        result: `Error: ${Array.isArray(data.error) ? data.error.join('\n') : data.error}`,
        type: 'message',
        message: 'Error'
      };
    }

    // Handle response format
    if (data.result !== undefined) {
      return {
        result: data.result,
        type: data.type,
        message: data.message,
        direction: data.direction
      };
    }

    // Fallback for backward compatibility
    return {
      result: data.java_code || '// No output.',
      type: 'converted_code',
      message: 'Conversion complete'
    };
  } catch (error) {
    return {
      result: 'Error: Could not connect to the server. Please try again.',
      type: 'message',
      message: 'Connection Error'
    };
  }
};