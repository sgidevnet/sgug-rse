# If the package needs to download data for the test which cannot be done in
# koji, these can be disabled in koji by using `bcond_with` instead, but the
# tests must be validated in mock with network enabled like so:
# mock -r fedora-rawhide-x86_64 rebuild <srpm> --enable-network --rpmbuild-opts="--with tests"
%bcond_with tests

%global pypi_name pyfim

%global desc %{expand: \
PyFIM is an extension module that makes several frequent item set mining
implementations available as functions in Python 2.7.x & 3.5.x. Currently
apriori, eclat, fpgrowth, sam, relim, carpenter, ista, accretion and apriacc
are available as functions, although the interfaces do not offer all of the
options of the command line program. (Note that lcm is available as an
algorithm mode of eclat.) There is also a "generic" function fim, which is
essentially the same function as fpgrowth, only with a simplified interface
(fewer options). Finally, there is a function arules for generating association
rules (simplified interface compared to apriori, eclat and fpgrowth, which can
also be used to generate association rules.

How to use the functions can be seen in the example scripts testfim.py and
testacc.py in the source package (directory pyfim/ex). From a Python script or
command prompt interface, call help(fim), help(apriori) (or help(fim.apriori)),
help(eclat) (or help(fim.eclat)) etc. or print, for example, apriori.__doc__,
eclat.__doc__ etc. for a description of the functions and their arguments.

This extension module was originally developed for Python 2.7. The shared
objects made available above were compiled particularly for Python 2.7.11 and
Python 3.5.1 on Ubuntu 16.04 LTS and the dynamic modules made available above
were compiled for Python 2.7.10 and Python 3.5.1 on Windows 10.}

Name:           python-%{pypi_name}
Version:        6.28
Release:        5%{?dist}
Summary:        Frequent Item Set Mining and Association Rule Induction

License:        MIT
URL:            http://www.borgelt.net/%{pypi_name}.html
Source0:        http://www.borgelt.net/src/%{pypi_name}.tar.gz

%{?python_enable_dependency_generator}

%description
%{desc}


%package -n python3-%{pypi_name}
Summary:        %{summary}
BuildRequires:  gcc
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist Cython}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%{desc}

%prep
%autosetup -c -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

# Remove date stamp from version
sed -i "s/version=.*/version='6.28',/" setup.py

# Comment out to remove /usr/bin/env shebangs
# Can use something similar to correct/remove /usr/bin/python shebangs also
# find . -type f -name "*.py" -exec sed -i '/^#![  ]*\/usr\/bin\/env.*$/ d' {} 2>/dev/null ';'

%build
%py3_build

%install
%py3_install

%check
%if %{with tests}
%{__python3} setup.py test
%endif

%files -n python3-%{pypi_name}
# All sub directories contain this file
%license pyfim/doc/mit-license.txt
%{python3_sitearch}/fim-%{version}-py3.?.egg-info
%{python3_sitearch}/fim.cpython-%{python3_version_nodots}*.so

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 6.28-5
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.28-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 6.28-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.28-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 12 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 6.28-1
- Use better file entry

* Mon Jun 10 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 6.28-1
- Initial build
