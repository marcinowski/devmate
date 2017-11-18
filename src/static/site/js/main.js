(function() {
    'use strict';
    angular
        .module('devMateApp')
        .controller('MainCtrl', ['$scope', '$controller', '$resource', '$compile',
            function ($scope, $controller, $resource, $compile) {
                angular.extend(this, $controller('SkeletonCtrl', {$scope: $scope}));
            }]);
})();
