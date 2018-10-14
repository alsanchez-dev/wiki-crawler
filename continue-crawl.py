# TODO: Implement the continue_crawl function described above


words = ['this1', 'this2', 'this3', 'this4', 'boshka', ]
url = ['https://en.wikipedia.org/wiki/Floating_point']
urls = ['https://en.wikipedia.org/wiki/Floating_point', 'https://en.wikipedia.org/wiki/Computing', 'https://en.wikipedia.org/wiki/Floating_point']
list_25 = [i for i in range(0,26)]

# Alternative solution
#
# def continue_crawl(search_history, target_url):
#
#     without_duplication = []
#     duplicated = 0
#
#     for i in search_history:
#         if i not in without_duplication:
#             without_duplication.append(i)
#         else:
#             duplicated = duplicated + 1
#
#
#     print(duplicated)
#
#     if search_history[-1] == target_url or len(search_history) > 25 or duplicated > 0:
#         return False
#
#     else:
#         return True


def continue_crawl(search_history, target_url):

    print(search_history[:-1])

    if search_history[-1] == target_url or len(search_history) > 25 or search_history[-1] in search_history[:-1]:
        return False

    else:
        return True


print(continue_crawl(urls, 'https://en.wikipedia.org/wiki/Philosophy'))
