from blueprints import auth_router

@auth_router.get("/")
async def default():
    print("default auth")
    return {"ok":True,"message":"default auth"}

@auth_router.get("/test/")
async def test():
    print("test auth")
    return {"ok":True,"message":"test auth"}

