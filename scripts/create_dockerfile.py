"""This script used to create dockerfile which can be used in Ali dockerhub to build gcr image"""

if __name__ == '__main__':
    with open('grc_image_list.csv', 'r') as fp:
        with open('dokcerfile_list.csv','w') as df_list:
            for line in fp.readlines():
                image = line.split(',')[1]
                version = 'latest'
                if len(image.split(':')) > 1:
                    version = image.split(':')[1]
                name = image.replace('gcr.io/', '').replace(f':', '_').replace('/', '_')
                dockerfile_name = f'Dockerfile_{name.strip()}'

                # ali dockerfile name limit
                if len(dockerfile_name) > 60:
                    dockerfile_name = dockerfile_name[:60]

                with open(f'dockerfiles/{dockerfile_name}', 'w') as dockerfile:
                    dockerfile.write(f"FROM {image}")

                df_list.write(f'{dockerfile_name},{version.strip()},{image.split(":")[0].replace("gcr.io/", "").replace("/", "_")},' + line)
