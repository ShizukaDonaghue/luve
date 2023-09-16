# LUVE | Testing

Return to [README](https://github.com/ShizukaDonaghue/luve)

## Code Validation

### HTML
All HTML pages were validated using [W3C HTML Validator](https://validator.w3.org/) to check for any issues or syntax errors. The only errors identified were related to Summernote fields and Clearable_file_input widget. Please see the results below for each page.

<details>
  <summary>Home Page - No issues or errors</summary>
  
  <img src="docs/images/testing/html-home-page.png">

</details>

<details>
  <summary>Sign Up Page - No issues or errors</summary>
  
  <img src="docs/images/testing/html-signup-page.png">

</details>

<details>
  <summary>Log In Page - No issues or errors</summary>
  
  <img src="docs/images/testing/html-login-page.png">

</details>


<details>
  <summary>Log Out Page - No issues or errors</summary>
  
  <img src="docs/images/testing/html-logout-page.png">

</details>

<details>
  <summary>Articles Page - No issues or errors</summary> 
  
  <img src="docs/images/testing/html-articles-page.png">

</details>

<details>
  <summary>Article Details Page - No issues or errors</summary> 
  
  <img src="docs/images/testing/html-article-detail-page.png">

</details>

<details>
  <summary>Add Article Page - Errors identified for Summernote fields & clearable_file_input widget</summary> 
  
  <img src="docs/images/testing/html-add-article-page-1.png">
  <img src="docs/images/testing/html-add-article-page-2.png">
  <img src="docs/images/testing/html-add-article-page-3.png">

</details>

There were 10 errors identified in total. The first 9 errors were related to the Summernote widget that is used in the article form. Since the errors resulted from Summernote codes, these were not addressed. The last error was related to clearable_file_input widget used for the image field within the form and thus this was not addressed as modifying it would break the code. While these errors were not addressed, they do not affect the functionality of the application.

<details>
  <summary>Edit Article Page - Errors identified for Summernote fields & clearable_file_input widget</summary> 
  
  <img src="docs/images/testing/html-edit-article-page-1.png">
  <img src="docs/images/testing/html-edit-article-page-2.png">
  <img src="docs/images/testing/html-edit-article-page-3.png">

</details>

There were 10 errors identified in total. The first 9 errors were related to the Summernote widget that is used in the article form. Since the errors resulted from Summernote codes, these were not addressed. The last error was related to clearable_file_input widget used for the image field within the form and thus this was not addressed as modifying it would break the code. While these errors were not addressed, they do not affect the functionality of the application.

<details>
  <summary>Shopping Bag Page - No issues or errors</summary> 
  
  <img src="docs/images/testing/html-bag-page.png">

</details>

<details>
  <summary>Checkout Page - No issues or errors</summary> 
  
  <img src="docs/images/testing/html-checkout-page.png">

</details>

<details>
  <summary>Checkout Success Page - No issues or errors</summary> 
  
  <img src="docs/images/testing/html-checkout-success-page.png">

</details>

<details>
  <summary>Contact Page - No issues or errors</summary> 
  
  <img src="docs/images/testing/html-contact-page.png">

</details>

<details>
  <summary>Contact Success Page - No issues or errors</summary> 
  
  <img src="docs/images/testing/html-contact-success-page.png">

</details>

<details>
  <summary>Products Page - No issues or errors</summary>
  
  <img src="docs/images/testing/html-products-page.png">

</details>

<details>
  <summary>Product Details Page - No issues or errors</summary> 
  
  <img src="docs/images/testing/html-product-detail-page.png">

</details>

<details>
  <summary>Add Product Page - Error identified for clearable_file_input widget</summary> 
  
  <img src="docs/images/testing/html-add-product-page.png">

</details>

One error was identified for the image field, which was related to clearable_file_input widget used within the product form. This error was not addressed as modifying the widget would break the code, however, it does not affect the functionality of the application.

<details>
  <summary>Edit Product Page - Error identified for clearable_file_input widget</summary> 
  
  <img src="docs/images/testing/html-edit-product-page.png">

</details>

One error was identified for the image field, which was related to clearable_file_input widget used within the product form. This error was not addressed as modifying the widget would break the code, however, it does not affect the functionality of the application.

<details>
  <summary>Edit Review Page - No issues or errors</summary> 
  
  <img src="docs/images/testing/html-edit-review-page.png">

</details>

<details>
  <summary>Profile Page - No issues or errors</summary> 
  
  <img src="docs/images/testing/html-profile-page.png">

</details>

<details>
  <summary>404 Error Page - No issues or errors</summary> 
  
  <img src="docs/images/testing/html-404-page.png">

</details>

<details>
  <summary>Wishlist Page - No issues or errors</summary> 
  
  <img src="docs/images/testing/html-wishlist-page.png">

</details>

<details>
  <summary>Privacy Policy Page - No issues or errors</summary> 
  
  <img src="docs/images/testing/html-privacy-policy.png">

</details>

<details>
  <summary>Terms and Conditions Page - No issues or errors</summary> 
  
  <img src="docs/images/testing/html-terms-conditions-page.png">

</details>

### CSS
CSS codes used in the application were validated using [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) and no issues or errors were found.

<details>
  <summary>Base CSS Codes - No issues or errors</summary> 
  
  <img src="docs/images/testing/css-validation.jpg">

</details>

<details>
  <summary>Checkout CSS Codes - No issues or errors</summary> 
  
  <img src="docs/images/testing/css-validation.jpg">

</details>

<details>
  <summary>Contact CSS Codes - No issues or errors</summary> 
  
  <img src="docs/images/testing/css-validation.jpg">

</details>

<details>
  <summary>Profile CSS Codes - No issues or errors</summary> 
  
  <img src="docs/images/testing/css-validation.jpg">

</details>


### JavaScript
JavaScript codes used in the application were validated using [JSHint](https://jshint.com/). While there were 2 undefined variables identified, there were no critical errors. Please see the results below for each file.

<details>
  <summary>Base JavaScript Codes - Undefined variable identified </summary> 
  
  <img src="docs/images/testing/js-base.png">

</details>

Undefined variable "checkout" was identified for the order form. This calls for `checkout()` function in checkout/views.py and not defined within the file. This was necessary as jQuery validation would submit the form before Stripe could processs the payment, causing the payment to fail (more details in [#86](https://github.com/ShizukaDonaghue/luve/issues/86)).

<details>
  <summary>Countryfield JavaScript Codes - No issues or errors</summary> 
  
  <img src="docs/images/testing/js-countryfield.png">

</details>

<details>
  <summary>Stripe Elements JavaScript Codes - Undefined variable identified</summary> 
  
  <img src="docs/images/testing/js-stripe-elements.png">

</details>

Undefined variable "Stripe" was identified, however, this was addressed as it belongs to the external Stripe API. 

### Python
Python codes used throughout the application were validated using [CI Python Linter](https://pep8ci.herokuapp.com/) and no issues or errors were found.
Please see the results for each page.

#### LUVE Project

<details>
  <summary>settings.py - No issues or errors</summary> 
  
  <img src="docs/images/testing/luve-settings.png">

</details>

Note: `# noqa` was added to Django generated codes under `AUTH_PASSWORD_VALIDATORS` and also Cloudinary storage under `STATICFILES_STORAGE` for "line too long" errors to be ignored as these could not be shortened.

<details>
  <summary>urls.py - No issues or errors</summary> 
  
  <img src="docs/images/testing/luve-urls.png">

</details>

<details>
  <summary>views.py - No issues or errors</summary> 
  
  <img src="docs/images/testing/luve-views.png">

</details>

#### Articles App

<details>
  <summary>admin.py - No issues or errors</summary> 
  
  <img src="docs/images/testing/articles-admin.png">

</details>

<details>
  <summary>forms.py - No issues or errors</summary> 
  
  <img src="docs/images/testing/articles-forms.png">

</details>

<details>
  <summary>models.py - No issues or errors</summary> 
  
  <img src="docs/images/testing/articles-models.png">

</details>

<details>
  <summary>urls.py - No issues or errors</summary> 
  
  <img src="docs/images/testing/articles-urls.png">

</details>

<details>
  <summary>validators.py - No issues or errors</summary> 
  
  <img src="docs/images/testing/articles-validators.png">

</details>

<details>
  <summary>views.py - No issues or errors</summary> 
  
  <img src="docs/images/testing/articles-views.png">

</details>

<details>
  <summary>widgets.py - No issues or errors</summary> 
  
  <img src="docs/images/testing/articles-widgets.png">

</details>

#### Bag App

<details>
  <summary>bag_tools.py - No issues or errors</summary> 
  
  <img src="docs/images/testing/bag-bag-tools.png">

</details>

<details>
  <summary>contexts.py - No issues or errors</summary> 
  
  <img src="docs/images/testing/bag-contexts.png">

</details>

<details>
  <summary>urls.py - No issues or errors</summary> 
  
  <img src="docs/images/testing/bag-urls.png">

</details>

<details>
  <summary>views.py - No issues or errors</summary> 
  
  <img src="docs/images/testing/bag-views.png">

</details>

#### Checkout App

<details>
  <summary>admin.py - No issues or errors</summary> 
  
  <img src="docs/images/testing/checkout-admin.png">

</details>

<details>
  <summary>forms.py - No issues or errors</summary> 
  
  <img src="docs/images/testing/checkout-forms.png">

</details>

<details>
  <summary>models.py - No issues or errors</summary> 
  
  <img src="docs/images/testing/checkout-models.png">

</details>

<details>
  <summary>signals.py - No issues or errors</summary> 
  
  <img src="docs/images/testing/checkout-signals.png">

</details>

<details>
  <summary>urls.py - No issues or errors</summary> 
  
  <img src="docs/images/testing/checkout-urls.png">

</details>

<details>
  <summary>views.py - No issues or errors</summary> 
  
  <img src="docs/images/testing/checkout-views.png">

</details>

<details>
  <summary>webhook_handler.py - No issues or errors</summary> 
  
  <img src="docs/images/testing/checkout-webhook-handler.png">

</details>

<details>
  <summary>webhooks.py - No issues or errors</summary> 
  
  <img src="docs/images/testing/checkout-webhooks.png">

</details>

#### Contact App

<details>
  <summary>admin.py - No issues or errors</summary> 
  
  <img src="docs/images/testing/contact-admin.png">

</details>

<details>
  <summary>forms.py - No issues or errors</summary> 
  
  <img src="docs/images/testing/contact-forms.png">

</details>

<details>
  <summary>models.py - No issues or errors</summary> 
  
  <img src="docs/images/testing/contact-models.png">

</details>

<details>
  <summary>urls.py - No issues or errors</summary> 
  
  <img src="docs/images/testing/contact-urls.png">

</details>

<details>
  <summary>views.py - No issues or errors</summary> 
  
  <img src="docs/images/testing/contact-views.png">

</details>

#### Home App

<details>
  <summary>contexts.py - No issues or errors</summary> 
  
  <img src="docs/images/testing/home-contexts.png">

</details>

<details>
  <summary>urls.py - No issues or errors</summary> 
  
  <img src="docs/images/testing/home-urls.png">

</details>

<details>
  <summary>views.py - No issues or errors</summary> 
  
  <img src="docs/images/testing/home-views.png">

</details>

#### Products App

<details>
  <summary>admin.py - No issues or errors</summary> 
  
  <img src="docs/images/testing/products-admin.png">

</details>

<details>
  <summary>forms.py - No issues or errors</summary> 
  
  <img src="docs/images/testing/products-forms.png">

</details>

<details>
  <summary>models.py - No issues or errors</summary> 
  
  <img src="docs/images/testing/products-models.png">

</details>

<details>
  <summary>urls.py - No issues or errors</summary> 
  
  <img src="docs/images/testing/products-urls.png">

</details>

<details>
  <summary>views.py - No issues or errors</summary> 
  
  <img src="docs/images/testing/products-views.png">

</details>

<details>
  <summary>widgets.py - No issues or errors</summary> 
  
  <img src="docs/images/testing/products-widgets.png">

</details>

#### Profiles App

<details>
  <summary>forms.py - No issues or errors</summary> 
  
  <img src="docs/images/testing/profiles-forms.png">

</details>

<details>
  <summary>models.py - No issues or errors</summary> 
  
  <img src="docs/images/testing/profiles-models.png">

</details>

<details>
  <summary>urls.py - No issues or errors</summary> 
  
  <img src="docs/images/testing/profiles-urls.png">

</details>

<details>
  <summary>views.py - No issues or errors</summary> 
  
  <img src="docs/images/testing/profiles-views.png">

</details>

### Wishlist App

<details>
  <summary>admin.py - No issues or errors</summary> 
  
  <img src="docs/images/testing/wishlist-admin.png">

</details>

<details>
  <summary>contexts.py - No issues or errors</summary> 
  
  <img src="docs/images/testing/wishlist-contexts.png">

</details>

<details>
  <summary>models.py - No issues or errors</summary> 
  
  <img src="docs/images/testing/wishlist-models.png">

</details>

<details>
  <summary>urls.py - No issues or errors</summary> 
  
  <img src="docs/images/testing/wishlist-urls.png">

</details>

<details>
  <summary>views.py - No issues or errors</summary> 
  
  <img src="docs/images/testing/wishlist-views.png">

</details>

## Lighthouse
Lighthouse in [Chrome Dev Tools](https://developer.chrome.com/docs/devtools/) was used to test accessibility and performance.
Please see the results below for each page.

<details>
  <summary>Home Page</summary>
  
  Desktop:  
  <img src="docs/images/testing/home-desktop.png">

  Mobile:  
  <img src="docs/images/testing/home-mobile.png">
	
</details>

<details>
  <summary>Articles Page</summary>
  
  Desktop:  
  <img src="docs/images/testing/articles-desktop.png">

  Mobile:  
  <img src="docs/images/testing/articles-mobile.png">
	
</details>

<details>
  <summary>Article Detail Page</summary>
  
  Desktop:  
  <img src="docs/images/testing/article-detail-desktop.png">

  Mobile:  
  <img src="docs/images/testing/article-detail-mobile.png">
	
</details>

<details>
  <summary>Add Article Page</summary>
  
  Desktop:  
  <img src="docs/images/testing/add-article-desktop.png">

  Mobile:  
  <img src="docs/images/testing/add-article-mobile.png">
	
</details>

<details>
  <summary>Shopping Bag Page</summary>
  
  Desktop:  
  <img src="docs/images/testing/bag-desktop.png">

  Mobile:  
  <img src="docs/images/testing/bag-mobile.png">
	
</details>

<details>
  <summary>Checkout Page</summary>
  
  Desktop:  
  <img src="docs/images/testing/checkout-desktop.png">

  Mobile:  
  <img src="docs/images/testing/checkout-mobile.png">
	
</details>

<details>
  <summary>Checkout Success Page</summary>
  
  Desktop:  
  <img src="docs/images/testing/checkout-success-desktop.png">

  Mobile:  
  <img src="docs/images/testing/checkout-success-mobile.png">
	
</details>



