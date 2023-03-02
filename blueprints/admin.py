from blueprints import admin_router

@admin_router.get("/")
async def default():
    print("default admin")
    return {"ok":True,"message":"default admin"}

@admin_router.get("/test/")
async def test():
    print("test admin")
    return {"ok":True,"message":"test admin"}

