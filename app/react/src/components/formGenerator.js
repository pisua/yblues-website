import React, { useState, useEffect } from 'react';
import { Form, TextField, SelectField, SubmitButton } from './formElements';

const formSchema = {
    name: {
        type: "text",
        label: "Name",
        required: true
    },
    email: {
        type: "email",
        label: "Email",
        required: true
    },
    role: {
        type: "select",
        label: "Role",
        required: true,
        options: [
            {
                label: "Admin",
                value: "admin"
            },
            {
                label: "User",
                value: "user"
            }
        ]
    }
}

export function FormGenerator() {
    const [formData, setFormData] = useState({});
    const [validationSchema, setValidationSchema] = useState({});

    useEffect(() => {
        initForm(formSchema);
    }, []);

    const initForm = (formSchema) => {
        let _formData = {};
        let _validationSchema = {};



        setFormData(_formData);
    }

    const getFormElement = (elementName, elementSchema) => {
        const props = {
            name: elementName,
            label: elementSchema.label,
            options: elementSchema.options
        };

        if (elementSchema.type === "text" || elementSchema.type === "email") {
            return <TextField {...props} />
        }

        if (elementSchema.type === "select") {
            return <SelectField  {...props} />
        }

    }

    const onSubmit = (values, { setSubmitting, resetForm, setStatus }) => {
        console.log(values);
        setSubmitting(false);
    }

    return (
        <div className="FormGenerator">
            <Form
                enableReinitialize
                initialValues={formData}
                validationSchema={validationSchema}
                onSubmit={onSubmit}
            >

                {Object.keys(formSchema).map( (key, ind) => (
                    <div key={key}>
                        {getFormElement(key, formSchema[key])}
                    </div>
                ))}

            </Form>
        </div>
    );
}

