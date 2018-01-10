import mymodule
movies = ["The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91,
          ["Graham Chapman", ["Michael Palin", "John Cleese",
                              "Terry Gilliam", "Eric Idle", 'Terry Jones']]]

mymodule.print_lo(movies)

# for each_item in movies:
#     if isinstance(each_item, list):
#         for nest_item in each_item:
#             if isinstance(nest_item,list):
#                 for deep_item in nest_item:
#                     print(deep_item)
#             else:
#                 print(nest_item)
#     else:
#         print(each_item)
