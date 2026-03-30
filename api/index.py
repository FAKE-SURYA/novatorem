from api.orchestrator import app

# Vercel specifically looks for one of these two variable names. 
# We are defining both just to make absolutely sure it can't miss it.
application = app
