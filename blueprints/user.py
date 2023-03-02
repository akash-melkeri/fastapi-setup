from blueprints import user_router

@user_router.get("/")
async def default():
    print("default user")
    return {"ok":True,"message":"default user"}

@user_router.get("/test/")
async def test():
    print("test user")
    return {"ok":True,"message":"test user"}
  
