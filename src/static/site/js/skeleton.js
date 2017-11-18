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
                $scope.showMediaFab = false;
            }
        ])
        .directive('imageSplash', function() {
            var imageSplashDefinition = {
                restrict: 'E',
                link: function (scope, element, attrs) {
                    scope.fontColor = attrs.fontColor || 'white';
                    var dim = attrs.dim || '0.8';
                    var css = {
                        backgroundPosition: 'center',
                        backgroundRepeat: 'no-repeat',
                        backgroundSize: 'cover',
                        backgroundImage: [
                            'linear-gradient(rgba(0,0,0,'+dim+'), rgba(0,0,0,'+dim+'))',
                            'url(' + attrs.image + ')',
                        ],
                        backgroundAttachment: 'fixed',
                        height: '50vh',
                    };
                    element.css(css);
                    scope.splashTitle = attrs.splashTitle;
                },
                templateUrl: 'directives/imageSplash.html',
            };
            return imageSplashDefinition;
        })
        .directive('scrollClass', function($window) {
            var scrollClassDefinition = {
                restrict: 'A',
                transclude: true,
                scope: {
                    scrollOffset: "@",
                    scrollToggleClass: "@"
                },
                template: '<ng-transclude></ng-transclude>',
                link: function (scope, element, attrs) {
                    angular.element($window).bind("scroll", function() {
                        element.toggleClass(scope.scrollToggleClass, this.pageYOffset >= parseInt(scope.scrollOffset));
                    });
                },
            };
            return scrollClassDefinition;
        })
        .directive('stickyScroll', function($window) {
            var stickyScrollDefinition = {
                restrict: 'E',
                transclude: true,
                templateUrl: 'directives/stickyScroll.html',
                scope: true,
                controller: function ($scope) {
                    $scope.scrollTop = function () {
                        $window.scrollTo(0,0);
                    }
                },
            };
            return stickyScrollDefinition;
        })
        .directive('navSearch', function() {
            var navSearchDefinition = {
                restrict: 'E',
                scope: true,
                templateUrl: 'directives/navSearch.html',
                link: function(scope, element, attrs) {

                },
                controller: function($scope) {
                    $scope.showInput = false;
                }
            };
            return navSearchDefinition;
        })
        .directive('articleCard', function() {
            var articleCardDefinition = {
                restrict: 'E',
                transclude: {
                    'title': 'articleTitle',
                    'date': 'articleDate',
                    'brief': '?articleBrief',
                },
                scope: {
                    imgUrl: "@",
                },
                templateUrl: 'directives/articleCard.html',
                controller: function($scope) {
                    $scope.showDescription = false;
                }
            };
            return articleCardDefinition;
        });
})();
