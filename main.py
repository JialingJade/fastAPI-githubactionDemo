from fastapi import FastAPI

#import uvicorn
import uvicorn

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}
    
@app.get("/tpgateway/coursecat")
async def tpgw_read_coursecat():
    return {"message": "tpgw_read_coursecat"}

@app.get("/tpgateway/coursesubcat/{cat_id}")
async def tpgw_read_coursesubcat(cat_id: int):
    if cat_id < 10:
        return {"cat_id": cat_id}
    else:
        return {"message": "bad catid"}

if __name__ == "__main__":
    uvicorn.run(app, port=8000, host="0.0.0.0")
    
    






