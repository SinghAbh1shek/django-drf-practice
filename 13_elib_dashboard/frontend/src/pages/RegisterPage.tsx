import { Button } from "@/components/ui/button"
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card"
import {
  Field,
  FieldDescription,
  FieldGroup,
  FieldLabel,
} from "@/components/ui/field"
import { Input } from "@/components/ui/input"
import { register } from "@/http/api"
import { useMutation } from "@tanstack/react-query"
import { LoaderCircle } from "lucide-react"
import { useRef } from "react"
import { Link, useNavigate } from "react-router"



const RegisterPage = () => 
  { 

  const navigate = useNavigate()

  const emailRef = useRef<HTMLInputElement>(null)
  const passwordRef = useRef<HTMLInputElement>(null)
  const fullnameRef = useRef<HTMLInputElement>(null)

  const mutation = useMutation({
    mutationFn: register,
    onSuccess: () => {
      console.log('register success')

      // redirect to dashboard
      navigate('/dashboard/home')
    }
  })

  const handleRegisterSubmit = () => {
    const email = emailRef.current?.value
    const password = passwordRef.current?.value
    const fullname = fullnameRef.current?.value

    if (!fullname || !email || !password){
      return alert('please enter email and password')
    }
    mutation.mutate({email, password, full_name:fullname})
  }


  return (
    <div className="flex justify-center items-center h-screen">
      <Card className="w-full max-w-sm">
        <CardHeader className="text-center">
          <CardTitle className="text-xl">Create your account</CardTitle>
          <CardDescription>
            Enter your email below to create your account
            {mutation.isError && <div className="text-red-500 text-sm">{'something went wrong'}</div>}
          </CardDescription>
        </CardHeader>
        <CardContent>
          <form>
            <FieldGroup>
              <Field>
                <FieldLabel htmlFor="name">Full Name</FieldLabel>
                <Input ref={fullnameRef} id="name" type="text" placeholder="John Doe" required />
              </Field>
              <Field>
                <FieldLabel htmlFor="email">Email</FieldLabel>
                <Input
                  ref={emailRef}
                  id="email"
                  type="email"
                  placeholder="m@example.com"
                  required
                />
              </Field>
              <Field>
                <Field>
                    <FieldLabel htmlFor="password">Password</FieldLabel>
                    <Input ref={passwordRef} id="password" type="password" required />
                </Field>
                <FieldDescription>
                  Must be at least 8 characters long.
                </FieldDescription>
              </Field>
              <Field>
                <Button type="button" onClick={handleRegisterSubmit} disabled={mutation.isPending}>
                  {mutation.isPending && <LoaderCircle className="animate-spin"/>}
                  <span>Create Account</span>
                </Button>
                <FieldDescription className="text-center">
                  Already have an account? <Link to={'/auth/login'}>Sign in</Link>
                </FieldDescription>
              </Field>
            </FieldGroup>
          </form>
        </CardContent>
      </Card>
    </div>
  )
}

export default RegisterPage
