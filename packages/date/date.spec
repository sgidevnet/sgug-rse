%global gitdate  20200207
%global commit   9a0ee2542848ab8625984fc8cdbfb9b5414c0082

%global scommit  %(c=%{commit}; echo ${c:0:7})
%global gitrel   %{?gitdate:.%{gitdate}git%{scommit}}
%global gitver   %{?gitdate:-%{gitdate}git%{scommit}}

%global abiver  2

Name:           date
Version:        2.4.1
Release:        1%{?gitrel}%{?dist}
Summary:        Date and time library based on the C++11/14/17 <chrono> header

License:        MIT
URL:            https://github.com/HowardHinnant/date
Source0:        %{url}/archive/%{commit}/%{name}-%{version}%{?gitver}.tar.gz
# add pkg-config support to make the package compatible with meson
Patch0:         %{url}/pull/538.patch#/output-date-pc-for-pkg-config.patch

BuildRequires:  cmake >= 3.7
BuildRequires:  gcc-c++
# required for test suite
BuildRequires:  tzdata

%description
%{summary}.


# only timezone libary has binary part
%package -n     libtz
Summary:        Timezone library built on top of the date library
Requires:       tzdata

%description -n libtz
Timezone library built on top of the date library. This timezone library
is a complete parser of the IANA timezone database. It provides for
an easy way to access all of the data in this database, using the types
from "date.h" and <chrono>. The IANA database also includes data on leap
seconds, and this library provides utilities to compute with that
information as well.


%package        devel
Summary:        Date and time library based on the C++11/14/17 <chrono> header
Requires:       libtz%{?_isa} = %{version}-%{release}
# virtual Provide for header-only parts of the library
Provides:       %{name}-static = %{version}-%{release}

%description    devel
This is actually several separate C++11/C++14/C++17 libraries:
 - "date.h" is a header-only library which builds upon <chrono>.
   It adds some new duration types, and new time_point types. It
   also adds "field" types such as year_month_day which is a
   struct {year, month, day}. And it provides convenient means
   to convert between the "field" types and the time_point types.
 - "tz.h" / "tz.cpp" are a timezone library built on top of the
   "date.h" library. This timezone library is a complete parser
   of the IANA timezone database. It provides for an easy way to
   access all of the data in this database, using the types from
   "date.h" and <chrono>. The IANA database also includes data
   on leap seconds, and this library provides utilities to compute
   with that information as well.
Slightly modified versions of "date.h" and "tz.h" were voted into
the C++20 working draft.

%prep
%autosetup -p1 -n %{name}-%{commit}
# remove broken tests
# fails due to gcc std::locale bugs (gcc#86976, HowardHinnant/date#388)
%{__rm} -f test/date_test/parse.pass.cpp
# fails in fedora-rawhide-i386 due to missing timezone configuration
%{__rm} -f test/tz_test/zoned_time_deduction.pass.cpp


%build
%cmake . \
    -DBUILD_TZ_LIB=ON     \
    -DUSE_SYSTEM_TZ_DB=ON \
    -DENABLE_DATE_TESTING=ON
%make_build


%install
%make_install


%check
%make_build testit


%files -n libtz
%license LICENSE.txt
%{_libdir}/*.so.%{abiver}*

%files devel
%license LICENSE.txt
%doc README.md
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*
%{_libdir}/*.so
%dir %{_libdir}/cmake/%{name}
%{_libdir}/cmake/%{name}/%{name}*.cmake
%{_libdir}/pkgconfig/%{name}.pc


%changelog
* Fri Feb 07 2020 Aleksei Bavshin <alebastr89@gmail.com> - 2.4.1-1.20200207git9a0ee254
- Initial import (#1801013)
