import { useEffect, useState } from "react";
import axios from "../axiosConfig";
import { Link, useParams } from "react-router-dom";

const Profile = () => {
  const { id } = useParams();
  console.log("ID is", id);

  const [userData, setUserData] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  useEffect(() => {
    console.log("In use effect", id);

    const fetchUserData = async () => {
      //if id is present load profile with given id
      if (id) {
        console.log("In id");

        try {
          setLoading(true);
          const respones = await axios.get("profiles/" + id, {});
          setLoading(false);
          setUserData(respones.data);
          console.log(respones.data);
        } catch (err) {
          setError("Error occured while fetching profile with id:", id);
          setLoading(false);
          console.log(err);
        }
      }
      // if no id is passed,then display self profile
      else {
        console.log("not In id");

        const username = localStorage.getItem("username");
        const password = localStorage.getItem("password");
        const profileId = localStorage.getItem("id");

        if (username && password) {
          try {
            setLoading(true);
            const response = await axios.get(`profiles/${profileId}`, {});
            setLoading(false);
            console.log(response.data);
            setUserData(response.data);
          } catch (error) {
            setError("Failed to load user profile data.", error);
            setLoading(false);
          }
        } else {
          setError("User not logged in.");
        }
      }
    };
    console.log("calling fn");

    fetchUserData();
  }, []);

  // show 404 page
  if (error)
    return (
      <>
        <section className="bg-white min-h-screen dark:bg-gray-900">
          <div className="py-8 px-4 mx-auto max-w-screen-xl lg:py-16 lg:px-6">
            <div className="mx-auto max-w-screen-sm text-center">
              <h1 className="mb-4 text-7xl tracking-tight font-extrabold lg:text-9xl text-primary-600 dark:text-primary-500">
                404
              </h1>
              <p className="mb-4 text-3xl tracking-tight font-bold text-gray-900 md:text-4xl dark:text-white">
                Something went wrong.
              </p>
              <p className="mb-4 text-lg font-light text-gray-500 dark:text-gray-400">
                Sorry, please try later, we will work on this.{error}
              </p>

              <Link
                to="/"
                className="inline-flex text-white bg-primary-600 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:focus:ring-primary-900 my-4"
              >
                {" "}
                Back to Homepage
              </Link>
            </div>
          </div>
        </section>
      </>
    );

  //show loading
  if (loading) return <>loading</>;

  //show profile data
  return (
    <>
      <section className="py-8 bg-white  min-h-screen md:py-16 dark:bg-gray-900 antialiased">
        <div className="max-w-screen-xl px-4 mx-auto 2xl:px-0">
          <div className="lg:grid lg:grid-cols-2 lg:gap-8 xl:gap-16">
            <div className="shrink-0 max-w-md lg:max-w-lg mx-auto">
              <img
                className="w-full dark:hidden"
                src="https://flowbite.s3.amazonaws.com/blocks/e-commerce/imac-front.svg"
                alt=""
              />
              <img
                className="w-full hidden dark:block"
                src="https://flowbite.s3.amazonaws.com/blocks/e-commerce/imac-front-dark.svg"
                alt=""
              />
            </div>
            <div className="mt-6 sm:mt-8 lg:mt-0">
              <h1 className="text-xl font-semibold text-gray-900 sm:text-2xl dark:text-white">
                Name:{userData.name}
              </h1>
              <div className="mt-4 sm:items-center sm:gap-4 sm:flex">
                <p className="text-2xl font-extrabold text-gray-900 sm:text-3xl dark:text-white">
                  {userData.address}
                </p>
              </div>

              <hr className="my-6 md:my-8 border-gray-200 dark:border-gray-800" />
              <p className="mb-6 text-gray-500 dark:text-gray-400">
                description
              </p>
            </div>
          </div>
        </div>
      </section>
    </>
  );
};

export default Profile;
