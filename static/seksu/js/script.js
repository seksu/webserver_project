
//myApp.directive('myDirective', function() {});
//myApp.factory('myService', function() {});

angular.module('myApp', [])
  .controller('myCtrl', ['$scope', function($scope) {

        $scope.count = 0;

        $scope.myFunc = function() {

                $scope.count++;
        };

        $scope.submit = function() {
                $scope.name = 'Superhero';
        };

}]);
