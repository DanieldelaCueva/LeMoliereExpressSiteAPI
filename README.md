# LeMoliereExpressSiteAPI

## Site map

            'Articles': {
                        'Create': '/articles/article-create/',
                        'List': '/articles/article-list/',
                        'Detail': '/articles/article-detail/<int:pk>',
                        'Update': '/articles/article-update/<int:pk>',
                        'Delete': '/articles/article-delete/<int:pk>',
                        'Validate': '/articles/article-validate/<int:pk>',
                        'Invalidate': '/articles/article-invalidate/<int:pk>'
                    }

        'Authorization': {
            'Login': '/authorization/login/',
            'Logout': '/authorization/logout/',
            'User List': '/authorization/user-list',
            'User Detail' : '/authorization/user-detail/<str:username>',
            'Change Password': '/authorization/change-password/<str:username>'
        }
 
