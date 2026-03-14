export interface User {
    id: number
    username: string
    email: string
    is_active: boolean
}

export interface Transaction {
    id: number
    amount: number
    description: string | null
    date: string
    user_id: number
}

export interface Token {
    access_token: string
    token_type: string
}

export interface TransactionCreate {
    amount: number
    description?: string
    type: "income" | "expense"
}

export interface AuthForm {
    password: string
    username: string
}

export interface RegisterForm {
    email: string
    username: string
    password: string
}