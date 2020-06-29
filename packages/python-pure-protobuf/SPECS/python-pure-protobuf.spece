%global pypi_name pure-protobuf

Name:           python-%{pypi_name}
Version:        2.0.0
Release:        3%{?dist}
Summary:        Python implementation of Protocol Buffers data types with dataclasses support

License:        MIT
URL:            https://github.com/eigenein/protobuf

# Using github sources since tests not available on PyPI
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel >= 3.7
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(setuptools)

%global _description %{expand:
pure-protobuf allows you to take advantages of the standard dataclasses module
to define message types. It is preferred over the legacy interface for new
projects. The dataclasses interface is available in Python 3.6 and higher.

The legacy interface is deprecated and still available via pure_protobuf.legacy.

This guide describes how to use pure-protobuf to structure your data. It tries
to follow the standard developer guide. It also assumes that you're familiar
with Protocol Buffers.}

%description %{_description}


%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name} %{_description}


%prep
%autosetup -n protobuf-%{version}

# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

# Fix shebangs
pushd pure_protobuf
sed -i 's|/usr/bin/env python3|%{_bindir}/python3|' \
    __init__.py dataclasses_.py
popd


%build
%py3_build


%install
%py3_install

# E: non-executable-script
pushd %{buildroot}%{python3_sitelib}/pure_protobuf/
chmod +x __init__.py dataclasses_.py
popd


%check
%{python3} -m pytest -v


%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/pure_protobuf-%{version}-py*.egg-info
%{python3_sitelib}/pure_protobuf/
%{python3_sitelib}/tests


%changelog
* Fri May 29 2020 Lyes Saadi <fedora@lyes.eu> - 2.0.0-3
- Removing useless dependencies (coverage/linting)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.0.0-2
- Rebuilt for Python 3.9

* Fri Feb 21 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 2.0.0-1
- Initial package
