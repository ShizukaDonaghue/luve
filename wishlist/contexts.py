from .models import Wishlist


def wishlist_count(request):
    """
    Makes the number of items in the user's wishlist available for the navbar
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
