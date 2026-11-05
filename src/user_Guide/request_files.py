#  I can define files to be uploaded by the client using File

from typing import Annotated
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.post("/file/")
async def create_file(file: Annotated[bytes | None, File(description="A file read as bytes")] = None): # optional and additional metadata file 
    if not file:
        return {"message": "No file sent"}
    return {"file_size":len(file)}


@app.post("/uploadedfile1/")
async def create_upload_file1(file: UploadFile | None = None):
    if not file:
        return {"message": "No upload file sent"}
    
    # contents = file.file.read() -> I am inside a noraml "def" path operation function
    contents = await file.read()
    return {"file_name": file.filename}


@app.post("/uploadedfile2/")
async def create_upload_file2(file: Annotated[UploadFile, File(description="A file read as UploadFile")],):
    if not file:
        return {"message": "No upload file sent"}
    
    # contents = file.file.read() -> I am inside a noraml "def" path operation function
    contents = await file.read()
    return {"file_name": file.filename}

#  Multiple File Upload with Additional Metadata

@app.post("/files/")
async def create_files(
    files: Annotated[list[bytes], File(description="Multiple files as bytes")],
):
    return {"file_sizes": [len(file) for file in files]}


@app.post("/uploadfiles/")
async def create_upload_files(
    files: Annotated[
        list[UploadFile], File(description="Multiple files as UploadFile")
    ],
):
    return {"filenames": [file.filename for file in files]}

@app.get("/")
async def main():
    content = """
<body>
<form action="/files/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
<form action="/uploadfiles/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
</body>
    """
    return HTMLResponse(content=content)