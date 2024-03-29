var launchCodeTvApp = angular.module('application', []);

launchCodeTvApp.controller('OntologyController', function ($scope, $http) {
  var app = this;
  $scope.bricks = [];


  $scope.hide = function(square) {
    _.remove($scope.bricks, function(current) { return current._id === square.brick._id });
  };

  $scope.more = function() {
    $http.get($scope.nextPage).success(function(data) {
      $scope.nextPage = data._links.next.href
      for (var i = 0; i < data._items.length; i++ ){
        $scope.bricks.push(data._items[i]);
      }
    }).error(function(data) {
      console.log('Error getting next page!!!!')
    });
  }

  $http.get('api/v1/nodes').success(function(data) {
    $scope.nextPage = data._links.next.href;
    for (var i = 0; i < data._items.length; i++ ){
      $scope.bricks.push(data._items[i]);
    }

    console.log('lets stop here');
  }).error(function(data) {
    console.log('Error getting nodes!!');
  });
});