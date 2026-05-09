import { Button } from "@/components/ui/button";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Field, FieldDescription, FieldGroup, FieldLabel } from "@/components/ui/field";
import { Input } from "@/components/ui/input";
import { login } from "@/http/api";
import { useMutation } from "@tanstack/react-query";
import { LoaderCircle } from "lucide-react";
import { useRef } from "react";
import { Link, useNavigate } from "react-router";

const LoginPage = () => {
  const navigate = useNavigate()

  const emailRef = useRef<HTMLInputElement>(null)
  const passwordRef = useRef<HTMLInputElement>(null)

  const mutation = useMutation({
    mutationFn: login,
    onSuccess: () => {
      console.log('login success')

      // redirect to dashboard
      navigate('/dashboard/home')
    }
  })

  const handleLoginSubmit = () => {
    const email = emailRef.current?.value
    const password = passwordRef.current?.value

    console.log('data: ', {email, password})

    if (!email || !password){
      return alert('please enter email and password')
    }
    mutation.mutate({email, password})
  }

    return (
        <div className="flex justify-center items-center h-screen">
      <Card className="w-full max-w-sm">
        <CardHeader>
          <CardTitle>Login to your account</CardTitle>
          <CardDescription>
            Enter your email below to login to your account
          </CardDescription>
        </CardHeader>
        <CardContent>
          <form>
            <FieldGroup>
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
                <div className="flex items-center">
                  <FieldLabel htmlFor="password">Password</FieldLabel>
                  <a
                    href="#"
                    className="ml-auto inline-block text-sm underline-offset-4 hover:underline"
                  >
                    Forgot your password?
                  </a>
                </div>
                <Input ref={passwordRef} id="password" type="password" required />
              </Field>
              <Field>
                <Button type="button" onClick={handleLoginSubmit} disabled={mutation.isPending}>
                  {mutation.isPending && <LoaderCircle className="animate-spin"/>}
                  <span>Login</span>
                  </Button>
                <FieldDescription className="text-center">
                  Don&apos;t have an account? <Link to={'/auth/register'}>Sign up</Link>
                </FieldDescription>
              </Field>
            </FieldGroup>
          </form>
        </CardContent>
      </Card>
     </div>
    )
}

export default LoginPage;