/*jslint browser: true, nomen: true, stupid: true, todo: true */
/*jshint -W097 */
/*global ludojApp, $ */

'use strict';

ludojApp.controller('NavController', function NavController(
    $location,
    $rootScope,
    $scope
) {
    function updatePath() {
        $scope.path = $location.path();
    }

    $rootScope.$on('$locationChangeSuccess', function () {
        $('.navbar-collapse').collapse('hide');
        updatePath();
    });

    updatePath();
});

ludojApp.controller('FooterController', function FooterController($scope) {
    $scope.yearNow = new Date().getFullYear();
});