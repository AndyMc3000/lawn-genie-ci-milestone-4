##### <br> #####
<a name="top-of-page"><img src="/readme/readme-assets/logo/lawn-genie-nav-logo-v4-resized-546-x-150px.png" width="300"></a>

# LawnGenie - Database Schema :floppy_disk: #

## Heroku PostgreSQL Database Schema ## 

The below Schema shows the tables, and the key:value pairs associated with each table in the Heroku Postgres database. The tables created specifically for the LawnGenie website are listed first in alphabetical order. Following that list, the built-in Django tables are listed.

            # - Tables unique to LawnGenie project
            blog_post
            {
                id: PrimaryKey
                title: String
                slug: String
                image: String
                updated_on: Date
                content: TextField
                created_on: Date
                status: IntegerField
                author: ForeignKey
            }

            checkout_order
            {
                id: PrimaryKey
                order_number: String
                full_name: String
                email: String
                phone_number: String
                country: String
                postcode: String
                town_or_city: String
                street_address1: String
                street_address2: String
                county: String
                date: Date
                delivery_cost: DecimalField
                order_total: DecimalField
                grand_total: DecimalField
                original_cart: TextField
                stripe_pid: String
                user_profile: ForeignKey
            }

            checkout_orderlineitem
            {
                id: PrimaryKey
                product_size: String
                quantity: IntegerField
                lineitem_total: DecimalField
                order: ForeignKey
                product: ForeignKey
            }

            newsletter_emailmessage
            {
                id: PrimaryKey
                emailtitle: String
                emailbody: TextField
            }

            newsletter_newslettersubscribers
            {
                id: PrimaryKey
                email: String
                date: Date
            }

            products_category
            {
                id: PrimaryKey
                name: String
                friendly_name: String
            }

            products_product
            {
                id: PrimaryKey
                sku: String
                name: String
                brand: String
                description: TextField
                price: DecimalField
                rating: DecimalField
                image: String
                category: ForeignKey
                has_sizes: Boolean
            }

            profiles_userprofile
            {
                id: PrimaryKey
                default_phone_number: String
                default_country: String
                default_postcode: String
                default_town_or_city: String
                default_street_address1: String
                default_street_address2: String
                default_county: String
                user: String
            }

            # - Built-in Django Tables
            account_emailaddress
            {
                id: PrimaryKey
                email: String
                verified: Boolean
                primary: Boolean
                user: ForeignKey
            }

            account_emailconfirmation
            {
                id: PrimaryKey
                created: Date
                sent: Date
                key: String
                email_address: ForeignKey
            }

            auth_group
            {
                name: String
            }

            auth_group_permissions
            {
                id: PrimaryKey
                group: ForeignKey
                permission: ForeignKey
            }

            auth_permission
            {
                name: String
                content_type: ForeignKey
                codename: String
            }

            auth_user
            {
                password: String
                last_login: Date
                is_superuser: Boolean
                username: String
                first_name: String
                last_name: String
                email: String
                is_staff: Boolean
                is_active: Boolean
                date_joined: Date
            }

            auth_user_groups
            {
                id: PrimaryKey
                user: ForeignKey
                group: ForeignKey
            }

            auth_user_user_permissions
            {
                id: PrimaryKey
                user: ForeignKey
                permission : ForeignKey
            }

            django_admin_log
            {
                action_time: Date
                object_id: TextField
                object_repr: String
                action_flag: SmallIntegerField
                change_message: TextField
                content_type: ForeignKey
                user: ForeignKey
            }

            django_content_type
            {
                app_label: String
                model: String
            }

            django_migrations
            {
                id: PrimaryKey
                app: String
                name: String
                applied: Date
            }

            django_session
            {
                session_key: String
                session_data: TextField
                expire_date: Date
            }

            django_site
            {
                domain; String
                name: String
            }

            socialaccount_socialaccount
            {
                id: PrimaryKey
                provider: String
                uid: String
                last_login: Date
                date_joined: Date
                extra_data: TextField
                user: ForeignKey
            }

            socialaccount_socialapp
            {
                id: PrimaryKey
                provider: String
                name: String
                client_id: String
                secret: String
                key: String
            }

            socialaccount_socialapp_sites
            {
                id: PrimaryKey
                socialapp_id: BigIntegerField
                site: ForeignKey
            }

            socialaccount_socialtoken
            {
                id: PrimaryKey
                token: TextField
                token_secret: TextField
                expires_at: Date
                account: ForeignKey
                app: ForeignKey
            }
