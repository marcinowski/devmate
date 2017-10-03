(function() {
    'use strict';
    angular
        .module('devMateApp', ['ngMaterial', 'ngResource'])
        .config(function($mdThemingProvider, $resourceProvider, $httpProvider) {
            $mdThemingProvider
                .theme('default')
                .primaryPalette('teal');
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
                            .ariaLabel('Portfolio Error')
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
        }])
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
        });
})();