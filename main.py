from typing import Union

from fastapi import FastAPI, Request, File, UploadFile
from starlette.requests import Request
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import numpy as np
import io
import cv2
import pytesseract


app = FastAPI()


@app.get("/")
def read_root():
	return {"Hello": "World"}


def read_img(img):
	text = pytesseract.image_to_string(img)
	return(text)


@app.post("/extract_text") 
async def extract_text(file: UploadFile):
	contents = await file.read()
	image_stream = io.BytesIO(contents)
	image_stream.seek(0)
	file_bytes = np.asarray(bytearray(image_stream.read()), dtype=np.uint8)
	frame = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
	label =  read_img(frame)
	return {"label": label}
