%global pypi_name readme_renderer
%global pkg_name readme-renderer

Name:           python-%{pkg_name}
Version:        26.0
Release:        3%{?dist}
Summary:        Library for rendering "readme" descriptions for Warehouse

License:        ASL 2.0
URL:            https://github.com/pypa/readme_renderer
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
Readme Renderer Readme Renderer is a library that will safely render arbitrary
README files into HTML. It is designed to be used in Warehouse_ to render the
long_description for packages. It can handle Markdown, reStructuredText (.rst),
and plain text.

%package -n     python3-%{pkg_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-bleach
# Review: https://bugzilla.redhat.com/show_bug.cgi?id=1827045
#BuildRequires:  python3-cmarkgfm
BuildRequires:  python3-docutils
BuildRequires:  python3-pygments
BuildRequires:  python3-setuptools
BuildRequires:  python3-six
%{?python_provide:%python_provide python3-%{pkg_name}}
 
%description -n python3-%{pkg_name}
Readme Renderer Readme Renderer is a library that will safely render arbitrary
README files into HTML. It is designed to be used in Warehouse_ to render the
long_description for packages. It can handle Markdown, reStructuredText (.rst),
and plain text.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

#%check
#%{__python3} setup.py test

%files -n python3-%{pkg_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py*.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 26.0-3
- Rebuilt for Python 3.9

* Mon May 18 2020 Fabian Affolter <mail@fabian-affolter.ch> - 26.0-2
- Fix naming (rhbz#1834176)

* Thu Apr 23 2020 Fabian Affolter <mail@fabian-affolter.ch> - 26.0-1
- Update to latest upstream release 26.0 (rhbz#1813626)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 24.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 24.0-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 24.0-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 24.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 24.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Dec 05 2018 Randy Barlow <bowlofeggs@fedoraproject.org> - 24.0-1
- Initial package.
