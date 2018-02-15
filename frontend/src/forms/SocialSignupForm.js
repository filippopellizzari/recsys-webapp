import React from "react";
import { Form, Button, Dropdown } from "semantic-ui-react";
import PropTypes from "prop-types";

import InlineError from "../messages/InlineError";
import {AGE_OPTIONS, COUNTRY_OPTIONS } from "./options";
import { getCountryName } from "./country";

class SocialSignupForm extends React.Component {
  state = {
    data: {
      age:"",
      country:""
    },
    loading: false,
    errors: {},
    serverErrors: {},
  };

  onChangeAge = (e,data) =>
    this.setState(
      {...this.state, data: { ...this.state.data, age: data.value }}
    );
  onChangeCountry = (e,data) =>
    this.setState(
      {...this.state,
        data: { ...this.state.data, country: getCountryName(data.value.toUpperCase()) }}
    );

  onSubmit = e => {
    e.preventDefault();
    const errors = this.validate(this.state.data);
    this.setState({ errors });
    if (Object.keys(errors).length === 0) {
      this.setState({ loading: true });
      this.props.submit(this.state.data)
    }
  };

  validate = data => {
    const errors = {};

    if (!data.age) {
      errors.age = "Required.";
    }
    if (!data.country) {
      errors.country = "Required.";
    }

    return errors;
  };

  render() {
    const { errors, loading } = this.state;

    return (
      <Form onSubmit={this.onSubmit} loading={loading}>
        <Form.Field error={!!errors.age}>
          <label htmlFor="age">Age</label>
            <Dropdown
              selection
              options={AGE_OPTIONS}
              onChange={this.onChangeAge}
            />
          {errors.age && <InlineError text={errors.age} />}
        </Form.Field>

        <Form.Field error={!!errors.country}>
          <label htmlFor="country">Country</label>
            <Dropdown
              search
              selection
              options={COUNTRY_OPTIONS}
              onChange={this.onChangeCountry}
            />
          {errors.country && <InlineError text={errors.country} />}
        </Form.Field>
        <Button primary fluid>Next</Button>
      </Form>
    );
  }
}

SocialSignupForm.propTypes = {
  submit: PropTypes.func.isRequired
};

export default SocialSignupForm;
