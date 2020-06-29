# The extracted tar has the commit in it
%global commit 9ae2e1f8b70fd6e1a5b8fb14925c2b51ef4fa6c3
%global shortcommit %(c=%{commit}; echo ${c:0:7})


%bcond_without tests

%global srcname pymatreader

%global desc %{expand: \
A Python module to read Matlab files. This module works with both the old (<
7.3) and the new (>= 7.3) HDF5 based format. The output should be the same for
both kinds of files.

Documentation can be found here: http://pymatreader.readthedocs.io/en/latest/}

Name:           python-%{srcname}
Version:        0.0.23
Release:        2%{?dist}
Summary:        Convenient reader for Matlab mat files

License:        BSD
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        https://gitlab.com/obob/%{srcname}/-/archive/%{commit}/%{srcname}-%{shortcommit}.tar.gz


BuildArch:      noarch

%{?python_enable_dependency_generator}

%description
%{desc}

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist future}
BuildRequires:  %{py3_dist h5py}
BuildRequires:  %{py3_dist nose}
BuildRequires:  %{py3_dist numpy}
BuildRequires:  %{py3_dist scipy}
BuildRequires:  %{py3_dist sphinx}
BuildRequires:  %{py3_dist sphinx_rtd_theme}
BuildRequires:  %{py3_dist setuptools}
BuildRequires:  %{py3_dist twine}
BuildRequires:  %{py3_dist wheel}
BuildRequires:  %{py3_dist xmltodict}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%{desc}

%package doc
Summary:        %{summary}

%description doc
Documentation for %{name}.

%prep
%autosetup -n %{srcname}-%{commit}
rm -rf %{srcname}.egg-info

%build
%py3_build

pushd doc
    make SPHINXBUILD=sphinx-build-3 html
    rm -rf build/html/.doctrees
    rm -rf build/html/.buildinfo
    # conver to utf8
    pushd build/html
        iconv --from=ISO-8859-1 --to=UTF-8 objects.inv > objects.inv.new && \
        touch -r objects.inv objects.inv.new && \
        mv objects.inv.new objects.inv
    popd
popd

%install
%py3_install

%check
%if %{with tests}
nosetests-%{python3_version}
%endif

%files -n python3-%{srcname}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{srcname}-%{version}-py3.?.egg-info
%{python3_sitelib}/%{srcname}

%files doc
%license LICENSE
%doc doc/build/html

%changelog
* Thu Jun 25 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.0.23-2
- Explicitly BR setuptools

* Sun Jun 21 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.0.23-1
- Update to 0.0.23

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.0.21-2
- Rebuilt for Python 3.9

* Sat Feb 01 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.0.21-1
- Update to latest release

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.19-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.0.19-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.0.19-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Apr 08 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.0.19-1
- Update to latest upstream release 0.0.19

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Nov 20 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.0.17-1
- Initial build
