from .models import Wishlist


def wishlist_count(request):
    """
    Make the number of items in the user's wishlist available for the navbar
    """
    if request.user.is_authenticated:
        return {
            'wishlist_count': Wishlist.objects.filter(
                user=request.user).count()
        }
    else:
        return {
            'wishlist_count': 0
        }


def user_wishlist(request):
    """
    Create a wishlist for the user
    """
    user = request.user
    user_wishlist = []
    if user.is_authenticated:
        wishlist = Wishlist.objects.filter(user=request.user)
        for item in wishlist:
            user_wishlist.append(item.product)
    return {
        'user_wishlist': user_wishlist,
    }
