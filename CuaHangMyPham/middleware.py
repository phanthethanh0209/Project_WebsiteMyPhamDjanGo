# class GlobalSessionMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         # Gán giá trị cho session ở đây
#         if 'user' not in request.session:
#             request.session['user'] = None
        
#         response = self.get_response(request)
#         return response