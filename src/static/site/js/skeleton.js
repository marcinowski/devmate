(function() {
    'use strict';
    angular
        .module('devMateApp', ['ngMaterial', 'ngResource', 'ngAnimate'])
        .config(function($mdThemingProvider, $resourceProvider, $httpProvider, $mdIconProvider) {
            $mdThemingProvider.definePalette('white', {
                '50': 'ffffff',
                '100': 'ffffff',
                '200': 'ffffff',
                '300': 'ffffff',
                '400': 'ffffff',
                '500': 'ffffff',
                '600': 'ffffff',
                '700': 'ffffff',
                '800': 'ffffff',
                '900': 'ffffff',
                'A100': 'ffffff',
                'A200': 'ffffff',
                'A400': 'ffffff',
                'A700': 'ffffff',
                'contrastDefaultColor': 'dark'
            });
            $mdThemingProvider.theme('default')
                .primaryPalette('white')
                .accentPalette('white')
                .backgroundPalette('white');
            $mdIconProvider.iconSet('social', '/static/js/social.svg', 24);
            $resourceProvider.defaults.stripTrailingSlashes = false;
            $httpProvider.defaults.xsrfCookieName = 'csrftoken';
            $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
        })
        .controller('SkeletonCtrl', ['$scope', '$mdDialog',
            function ($scope, $mdDialog) {
                $scope.showErrorDialog = function(){
                    $mdDialog.show(
                        $mdDialog.alert()
                            .parent(angular.element(document.body))
                            .clickOutsideToClose(true)
                            .title('Oops!')
                            .textContent("Error fetching data. Please try again later")
                            .ariaLabel('Error')
                            .ok('Back.')
                            .targetEvent(ev)
                    );
                };
                $scope.parseErrorData = function(error){
                    var error_msg = [];
                    angular.forEach(error, function(value, key) {
                        this.push(value[0]);
                    }, error_msg);
                    return error_msg.join('\n');
                };
            }
        ])
        .directive('imageSplash', function() {
            return {
                restrict: 'E',
                transclude: true,
                link: function (scope, element, attrs) {
                    element.css({
                        backgroundPosition: 'center',
                        backgroundRepeat: 'no-repeat',
                        backgroundSize: 'cover',
                        backgroundImage: [
                            'linear-gradient(rgba(0,0,0,0.8), rgba(0,0,0,0.8))',
                            'url(' + attrs.image + ')'
                        ],
                        backgroundAttachment: 'fixed',
                        height: '50vh',
                    });
                },
                template: '<div flex layout-fill layout="column" layout-align="center center" ng-transclude></div>',
            }
        })
        .directive('stickyScroller', function($window) {
            return {
                restrict: 'A',
                transclude: true,
                scope: {
                    scrollOffset: "@",
                    scrollClass: "@"
                },
                template: '<ng-transclude></ng-transclude>',
                link: function (scope, element, attrs) {
                    angular.element($window).bind("scroll", function() {
                        if (this.pageYOffset >= parseInt(scope.scrollOffset)) {
                            element.addClass(scope.scrollClass);
                        } else {
                            element.removeClass(scope.scrollClass);
                        }
                    });
                },
            }
        })
        .directive('articleList', function() {
            return {
                restrict: 'E',
                scope: {
                    cards: "@",
                },
                template: '' +
                    '<div>' + 
                    '</div>',
                link: function(scope, element, attrs) {
                    // resource call on scrolling
                    // start spinner
                    // render results
                    // stop
                }
            }
        })
        .directive('articleCard', function() {
            return {
                restrict: 'E',
                transclude: {
                    'title': 'articleTitle',
                    'date': 'articleDate',
                    'brief': '?articleBrief',
                },
                scope: {
                    imgUrl: "@",
                },
                template: '' +
                    '<div layout-margin style="height: 200px; width: 800px">' +
                    '   <div class="card" style="background-image: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)), url({{ imgUrl }});">' +
                    '       <div class="card-title">' +
                    '           <p ng-transclude="date"></p>' +
                    '           <p style="font-size: 1.5em; padding: 0; margin: 0;" ng-transclude="title"></p>' +
                    '           <p ng-transclude="brief" style="display: none">No description for this article.</p>' +
                    '       </div>' +
                    '   </div>' +
                    '</div>',
                link: function(scope, element, attrs) {
                    element.on('mouseover', function(e) {
                        console.log(element);
                    });
                },
            }
        });
})();