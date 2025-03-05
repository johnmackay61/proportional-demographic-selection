CREATE TABLE population (
    id SERIAL PRIMARY KEY,
    sex VARCHAR(10) CHECK (sex IN ('male', 'female')),
    age_group VARCHAR(10) CHECK (age_group IN ('18-30', '31-50', '51+')),
    income VARCHAR(10) CHECK (income IN ('low', 'middle', 'high')),
    family_status VARCHAR(10) CHECK (family_status IN ('single', 'married', 'other'))
);

CREATE TABLE seat_allocations (
    id SERIAL PRIMARY KEY,
    category VARCHAR(20),
    group_name VARCHAR(20),
    seat_count INT
);

CREATE TABLE selection_weights (
    id SERIAL PRIMARY KEY,
    person_id INT REFERENCES population(id),
    weight FLOAT
);

CREATE TABLE selected_legislators (
    id SERIAL PRIMARY KEY,
    person_id INT REFERENCES population(id),
    term_start DATE,
    term_end DATE
);
