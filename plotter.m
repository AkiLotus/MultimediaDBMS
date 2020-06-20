data = load('data.txt');
x = data(:, 1);
y_kd = data(:, 2);
m = length(y_kd); % number of training examples
y_bf = 7.659 * ones(m, 1);
accuracy = data(:, 3);
error = data(:, 4);

figure; % open a new figure window

% ====================== YOUR CODE HERE ======================
% Instructions: Plot the training data into a figure using the 
%               "figure" and "plot" commands. Set the axes labels using
%               the "xlabel" and "ylabel" commands. Assume the 
%               population and revenue data have been passed in
%               as the x and y arguments of this function.
%
% Hint: You can use the 'rx' option with plot to have the markers
%       appear as red crosses. Furthermore, you can make the
%       markers larger by using plot(..., 'rx', 'MarkerSize', 10);

hold on;
%plot(x, y_kd, 'r.', 'MarkerSize', 10); % Plot the data
%plot(x, y_bf, 'b.', 'MarkerSize', 10); % Plot the data
%plot(x, accuracy, 'c.', 'MarkerSize', 10); % Plot the data
plot(x, error, 'm.', 'MarkerSize', 10); % Plot the data
hold off;
%ylabel('execution time'); % Set the y?axis label
%ylabel('accuracy'); % Set the y?axis label
ylabel('error'); % Set the y?axis label
xlabel('tolerance'); % Set the x?axis label

sum(y_kd) / m

% ============================================================
