from fastapi import  HTTPException

def HTTPException() -> HTTPException:
    httpexception = HTTPException(status_code=404, detail={
        "error": "Resource not found",
        "message": "The requested resource does not exist on the server."
    })
    return httpexception