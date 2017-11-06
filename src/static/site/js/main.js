(function() {
    'use strict';
    angular
        .module('devMateApp')
        .controller('MainCtrl', ['$scope', '$controller',
            function ($scope, $controller) {
                angular.extend(this, $controller('SkeletonCtrl', {$scope: $scope}));
                $scope.progressCircular = true;
            }
        ]);
})();
