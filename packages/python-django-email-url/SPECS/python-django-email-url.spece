%global pypi_name dj-email-url
%global pkg_name django-email-url

Name:           python-%{pkg_name}
Version:        1.0.1
Release:        1%{?dist}
Summary:        Use an URL to configure email backend settings in your Django Application

License:        BSD
URL:            https://github.com/migonzalvar/dj-email-url
Source0:        %{pypi_source}
BuildArch:      noarch

%description
This utility allows to utilize the 12factor inspired environments variable to
configure the email backend in a Django application.

%package -n     python3-%{pkg_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-%{pkg_name}}

%description -n python3-%{pkg_name}
This utility allows to utilize the 12factor inspired environments variable to
configure the email backend in a Django application.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pkg_name}
%doc README.rst
%license LICENSE
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/dj_email_url.py
%{python3_sitelib}/dj_email_url-%{version}-py*.egg-info

%changelog
* Wed Jun 03 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.1-1
- Add license file
- Update to new upstream release 1.0.1

* Wed Jun 03 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.0-1
- Update to new upstream release 1.0.0

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.2.0-4
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 07 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.0-2
- Use var for source URL
- Better use of wildcards (rhbz#1786855)

* Sat Dec 28 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.0-1
- Initial package for Fedora
