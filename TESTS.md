## Table of contents
1. [Unit Testing](#unit-testing)
    - [Views](#views) 
    - [Forms](#forms)
- [Validator Testing](#validator-testing)
    - [PEP8](#pep8)
- [Manual Testing](#responsive-testing)
***

# Unit Testing
I have performed the following unit tests using the Red Green Refactor principle:

## Gallery Post List View

![Unit Tests for Gallery Post List View](static/screenshots_tests/gallery_list_view_unit_test.png)

Result:

![Unit Tests results](static/screenshots_tests/gallery_list_view_unit_test_results.png)

## Gallery Post Detail View

![Unit Tests for Gallery Post Detail View](static/screenshots_tests/gallery_post_detail_view_unit_test.png)

Result:

![Unit Tests results](static/screenshots_tests/gallery_post_detail_view_unit_test_results.png)

## Walk Post List View

![Unit Tests for Walk Post List View](static/screenshots_tests/walk_list_view_unit_test.png)

Result:

![Unit Tests results](static/screenshots_tests/walk_list_view_unit_test_results.png)

## Walk Post Detail View

![Unit Tests for Walk Post Detail View](static/screenshots_tests/walk_post_detail_view_unit_test.png)

Result:

![Unit Tests results](static/screenshots_tests/walk_post_detail_view_unit_test_results.png)

***

# Validator Testing

All python files passed through the PEP8 validator with no issues, apart from some long-line errors which were rectifed. One long-line error remains in settings.py (line 178): 
![Validator Test results for settings.py](static/screenshots_tests/validator_testing_settings.png)

***

# Manual Testing

## URL testing 
All urls were tested (development and deployed) and all worked as expected. 
![URL testing](static/screenshots_tests/url_testing.png)

## Crud testing
All apps were tested to ensure appropriate CRUD functionality was present in the development version of DRF.
![CRUD testing](static/screenshots_tests/crud_testing.png)

## Search Functionality testing
Search functionality was tested on Walk Posts and Gallery Posts, to ensure correct results were returned when searching by the relevant search fields for each app. 
![Search testing](static/screenshots_tests/search_testing.png)

