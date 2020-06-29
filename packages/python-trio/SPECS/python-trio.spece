# what it's called on pypi
%global srcname trio
# what it's imported as
%global libname %{srcname}
# name of egg info directory
%global eggname %{srcname}
# package name fragment
%global pkgname %{srcname}

%global common_description %{expand:
The Trio project's goal is to produce a production-quality, permissively
licensed, async/await-native I/O library for Python.  Like all async libraries,
its main purpose is to help you write programs that do multiple things at the
same time with parallelized I/O.  A web spider that wants to fetch lots of
pages in parallel, a web server that needs to juggle lots of downloads and
websocket connections at the same time, a process supervisor monitoring
multiple subprocesses... that sort of thing.  Compared to other libraries, Trio
attempts to distinguish itself with an obsessive focus on usability and
correctness.  Concurrency is complicated; we try to make it easy to get things
right.}

%bcond_without  tests


Name:           python-%{pkgname}
Version:        0.15.1
Release:        1%{?dist}
Summary:        An async/await-native I/O library for humans and snake people
License:        MIT or ASL 2.0
URL:            https://github.com/python-trio/trio
Source0:        %pypi_source
BuildArch:      noarch


%description %{common_description}


%package -n python3-%{pkgname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist setuptools}
%if %{with tests}
BuildRequires:  %{py3_dist pytest pyopenssl trustme}
BuildRequires:  %{py3_dist attrs sortedcontainers async-generator idna outcome sniffio}
%endif
%{?python_provide:%python_provide python3-%{pkgname}}


%description -n python3-%{pkgname} %{common_description}


%prep
%autosetup -n %{srcname}-%{version}
rm -rf %{eggname}.egg-info


%build
%py3_build


%install
%py3_install


%if %{with tests}
%check
%pytest --verbose trio/_core/tests
%endif


%files -n python3-%{pkgname}
%license LICENSE LICENSE.MIT LICENSE.APACHE2
%doc README.rst
%{python3_sitelib}/%{libname}
%{python3_sitelib}/%{eggname}-%{version}-py%{python3_version}.egg-info


%changelog
* Thu Jun 04 2020 Carl George <carl@george.computer> - 0.15.1-1
- Latest upstream rhbz#1828266

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.13.0-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 02 2020 Carl George <carl@george.computer> - 0.13.0-1
- Latest upstream rhbz#1742425

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.11.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.11.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Feb 28 2019 Carl George <carl@george.computer> - 0.11.0-1
- Latest upstream

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Sep 20 2018 Carl George <carl@george.computer> - 0.7.0-1
- Initial package
