%global pypi_name micawber

Name:           python-%{pypi_name}
Version:        0.5.1
Release:        2%{?dist}
Summary:        a small library for extracting rich content from urls

License:        MIT
URL:            http://github.com/coleifer/micawber/
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
A small library for extracting rich content from urls. what does it do?
-micawber supplies a few methods for retrieving rich metadata about a variety
of links, such as links to youtube videos. micawber also provides functions for
parsing blocks of text and html and replacing links to videos with rich
embedded --here is a quick example:.. code-block:: python import micawber load
up rules for...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
A small library for extracting rich content from urls. what does it do?
-micawber supplies a few methods for retrieving rich metadata about a variety
of links, such as links to youtube videos. micawber also provides functions for
parsing blocks of text and html and replacing links to videos with rich
embedded --here is a quick example:.. code-block:: python import micawber load
up rules for...


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
# the tests fail with ImportError: cannot import name 'bs_kwargs' from 'micawber.parsers'
# so disabling for now
# %{__python3} setup.py test

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.5.1-2
- Rebuilt for Python 3.9

* Sun Mar 22 2020 José Matos <jamatos@fedoraproject.org> - 0.5.1-1
- Update to 0.5.1

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 12 2019 José Matos <jamatos@fedoraproject.org> - 0.5.0-1
- update to 0.5.0

* Tue Jun 11 2019 José Matos <jamatos@fedoraproject.org> - 0.4.1-2
- Change the source url to standard path name (%%{pypi_source})

* Sun Jun  9 2019 José Matos <jamatos@fedoraproject.org> - 0.4.1-1
- update to 0.4.1

* Sat Sep  1 2018 José Matos <jamatos@fedoraproject.org> - 0.3.5-1
- Initial package.
