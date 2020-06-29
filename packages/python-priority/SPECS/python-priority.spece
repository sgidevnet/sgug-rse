# Created by pyp2rpm-3.3.2
%global pypi_name priority

%global common_description %{expand:
A HTTP/2 Priority Implementation Priority is a pure-Python
implementation of the priority logic for HTTP/2, set out in RFC 7540 Section
5.3 (Stream Priority)_. This logic allows for clients to express a preference
for how the server allocates its (limited) resources to the many outstanding
HTTP requests that may be running over a single HTTP/2 connection.}

Name:           python-%{pypi_name}
Version:        1.3.0
Release:        10%{?dist}
Summary:        A pure-Python implementation of the HTTP/2 priority tree

License:        MIT
URL:            http://python-hyper.org/priority/
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

# Increase deadline for test_period_of_repetition
Patch1:         deadline.patch

BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(hypothesis)

%{?python_enable_dependency_generator}

%description
%{common_description}


%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%{common_description}


%prep
%autosetup -n %{pypi_name}-%{version} -p1
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info


%build
%py3_build


%install
%py3_install


%check
PYTHONPATH=%{buildroot}%{python3_sitelib}:$PYTHONPATH %{__python3} -m pytest


%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info


%changelog
* Sun May 24 2020 Miro Hrončok <mhroncok@redhat.com> - 1.3.0-10
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep 09 2019 Miro Hrončok <mhroncok@redhat.com> - 1.3.0-8
- Subpackage python2-priority has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Aug 17 2019 Miro Hrončok <mhroncok@redhat.com> - 1.3.0-7
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Mar 07 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.3.0-5
- Add actual tests

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.3.0-2
- Rebuilt for Python 3.7

* Mon May 14 2018 Robert-André Mauchin <zebob.m@gmail.com> - 1.3.0-1
- Initial package.
