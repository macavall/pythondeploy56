import logging

import azure.functions as func

import asyncio

async def my_async_function():
    # Add your async code here
    await asyncio.sleep(1)  # For example, simulate an async operation
    
    return "Async function completed successfully!"

async def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    # Call the async function
    result = await my_async_function()

    return func.HttpResponse(f"{result}")