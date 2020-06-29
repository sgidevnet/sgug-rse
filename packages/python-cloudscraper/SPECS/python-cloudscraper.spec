# TODO: Add tests

%global pypi_name cloudscraper

Name:           python-%{pypi_name}
Version:        1.2.40
Release:        1%{?dist}
Summary:        Python module to bypass Cloudflare's anti-bot page

License:        MIT
URL:            https://github.com/venomous/cloudscraper
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%global _description %{expand:
A simple Python module to bypass Cloudflare's anti-bot page (also known as "I'm
Under Attack Mode", or IUAM), implemented with Requests. Cloudflare changes
their techniques periodically, so I will update this repo frequently.

This can be useful if you wish to scrape or crawl a website protected with
Cloudflare. Cloudflare's anti-bot page currently just checks if the client
supports Javascript, though they may add additional techniques in the future.

Due to Cloudflare continually changing and hardening their protection page,
cloudscraper requires a JavaScript Engine/interpreter to solve Javascript
challenges. This allows the script to easily impersonate a regular web browser
without explicitly deobfuscating and parsing Cloudflare's Javascript.}

%description %{_description}


%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%?python_enable_dependency_generator

%description -n python3-%{pypi_name} %{_description}


%prep
%autosetup -n %{pypi_name}-%{version}

# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info


%build
%py3_build


%install
%py3_install


%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{pypi_name}-%{version}-py*.egg-info
%{python3_sitelib}/%{pypi_name}/


%changelog
* Fri May 29 2020 Lyes Saadi <fedora@lyes.eu> - 1.2.40-1
- Update to 1.2.40

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.2.38-2
- Rebuilt for Python 3.9

* Thu May 21 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 1.2.38-1
- Update to 1.2.38

* Tue May 05 2020 Lyes Saadi <fedora@lyes.eu> - 1.2.36-1
- Update to 1.2.36

* Mon Apr 27 2020 Lyes Saadi <fedora@lyes.eu> - 1.2.34-1
- Update to 1.2.34

* Fri Apr 03 2020 Lyes Saadi <fedora@lyes.eu> - 1.2.33-1
- Update to 1.2.32 (GitHub) or 1.2.33 (PyPI)...

* Wed Apr 01 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 1.2.30-1
- Update to 1.2.30

* Tue Mar 10 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 1.2.26-1
- Update to 1.2.26

* Fri Feb 21 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 1.2.24-1
- Initial package
