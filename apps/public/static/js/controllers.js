'use strict';

angular.module('todoApp.controllers', [])
    .controller('BaseController', ['$scope', '$window', 'Restangular', 'SessionService', function ($scope, $window, Restangular, SessionService) {
        var current_user = SessionService.getUserSession();
        if (current_user == null || current_user.user_id == null) {
            Restangular.one('user/id').get()
                .then(function (data) {
                    SessionService.saveUserSession(data[0]);
                });
        }

        $scope.doLogout = function () {
            SessionService.removeUserSession();
            $window.location = '/logout';
        };
    }])
    .controller('LoginController', ['$scope', function ($scope) {
        $scope.user = {}

        $scope.hasError = function (field, validation) {
            if (validation) {
                return $scope.loginForm[field].$dirty && scope.loginForm[field].$error[validation];
            }
            return $scope.loginForm[field].$dirty && $scope.loginForm[field].$invalid;
        };
    }])
    .controller('HomeController', ['$scope', function ($scope) {
        $scope.heading = 'Home Page';
    }])

//    .controller('EditRecipeController', ['$scope', 'Restangular', 'SessionService',  function ($scope, Restangular, SessionService) {
//        $scope.recipe = {

    .controller('RecipeController', ['$scope', '$http', 'Restangular', 'SessionService', '$location', function ($scope, $http, Restangular, SessionService, $location) {
        $scope.recipe = {
            name: '',
            description: '',
            link: '',
            prep_time: '',
            instruction: '',
            temp: '',
            time: '',
            serv_size: ''
        }

        $scope.user = SessionService.getUserSession();
        var baseRecipe = Restangular.all('api/recipe');

        baseRecipe.customGETLIST($scope.user.user_id)
            .then(function (listResponse) {
                reloadRecipes(listResponse);
            });

        function reloadRecipes(data) {
            // Reloads the list of recipes into an array usable on the scope.

            $scope.recipe_list = [];
            for (var i = 0; i < data.length; i++) {
                var recipe = data[i].fields;
                recipe['id'] = data[i].pk;
//                if (!recipe['description']) {
//                    recipe['description'] = 'Empty';
//                }
                $scope.recipe_list.push(recipe);
            }
        }

        $scope.user = SessionService.getUserSession();
        $scope.addRecipe = function (recipe) {
            baseRecipe.all($scope.user.user_id).customPOST(recipe)
                .then(function (data) {
//                    reloadRecipe(data);
//                        toastr.success('You successfully added a new recipe!');
                    window.location = '/recipes';
                });
        }

        $scope.removeRecipe = function (recipe) {
            baseRecipe.all($scope.user.user_id).remove(recipe)
                .then(function (data) {
                    reloadRecipes(data);

                    toastr.success('You successfully removed your recipe!');
                });
        };
    }])


    .controller('TodoController', ['$scope', '$http', 'Restangular', 'SessionService', function ($scope, $http, Restangular, SessionService) {
        $scope.todos = [];
        $scope.types = {completed: false};

        $scope.user = SessionService.getUserSession();
        var baseTodo = Restangular.all('api/todo');

        baseTodo.customGETLIST($scope.user.user_id)
            .then(function (data) {
                reloadTodos(data);
            });

        $scope.addTodo = function (todo) {
            baseTodo.all($scope.user.user_id).customPOST(todo)
                .then(function (data) {
                    reloadTodos(data);
                    $scope.todo.title = '';
                    $scope.todo.description = '';

                    toastr.success('You successfully added a new todo!');
                });
        };

        $scope.changeCompleted = function (todo) {
            baseTodo.all($scope.user.user_id).customPUT(todo)
                .then(function (data) {
                    reloadTodos(data);

                    toastr.success('You successfully changed the status of your todo!');
                });
        };

        $scope.changeTitle = function (title, id) {
            var todo = {
                "id": id,
                "user": $scope.user.user_id,
                "title": title
            }

            baseTodo.all($scope.user.user_id).customPUT(todo)
                .then(function (data) {
                    reloadTodos(data);

                    toastr.success('You successfully changed the title of your todo!');
                });
        };

        $scope.changeDescription = function (description, id) {
            var todo = {
                "id": id,
                "user": $scope.user.user_id,
                "description": description
            }

            baseTodo.all($scope.user.user_id).customPUT(todo)
                .then(function (data) {
                    reloadTodos(data);
                    $scope.deleteButton = true;

                    toastr.success('You successfully changed the description of your todo!');
                });
        };

        $scope.removeTodo = function (todo) {
            baseTodo.all($scope.user.user_id).remove(todo)
                .then(function (data) {
                    reloadTodos(data);

                    toastr.success('You successfully removed your todo!');
                });
        };

        $scope.deleteButton = null;

        $scope.confirm = function () {
            $scope.deleteButton = true;
        };

        $scope.cancelDelete = function () {
            $scope.deleteButton = false;
        };

        function reloadTodos(data) {
            $scope.todos = [];
            for (var i = 0; i < data.length; i++) {
                var todo = data[i].fields;
                todo['id'] = data[i].pk;
                if (!todo['description']) {
                    todo['description'] = 'Empty';
                }
                $scope.todos.push(todo);
            }
        }
    }]);