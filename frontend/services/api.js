export const convertCode = async (code) => {
  try {
    const res = await fetch('http://localhost:8000/convert', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ code: code.trim() + '\n' }),
    });
    const data = await res.json();
    
    // Handle error response
    if (data.error) {
      return `Error: ${Array.isArray(data.error) ? data.error.join('\n') : data.error}`;
    }
    
    // Handle response format
    if (data.result !== undefined) {
      // Format output based on response type
      switch(data.type) {
        case 'output':
          return `${data.message}\n\n${data.result}`;
        case 'message':
          return `${data.message}\n${data.result}`;
        case 'grammar':
          return `${data.message}\n${data.result}`;
        case 'code':
          return `${data.message}\n\n${data.result}`;
        case 'converted_code':
          return `${data.message}\n\n${data.result}`;
        default:
          return data.result || '// No output.';
      }
    }
    
    // Fallback for backward compatibility
    return data.java_code || '// No output.';
  } catch (error) {
    return 'Error: Could not connect to the server. Please try again.';
  }
};