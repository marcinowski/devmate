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
        .controller('SkeletonCtrl', SkeletonCtrl);
            function SkeletonCtrl($scope, $mdDialog) {
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
            }
})();