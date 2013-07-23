%define commit 270dba8f8b757228efeac6b26cad3630eeb03030
%define shortcommit %(c=%{commit}; echo ${c:0:7})
Name:           stout
Summary:        A collection of C++ header only primitives 
Version:        0.1.0
Release:        1.%{shortcommit}%{?dist}
License:        ASL 2.0
URL:            https://github.com/3rdparty/stout
Group:          System Environment/Libraries
Source0:        https://github.com/3rdparty/stout/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz
BuildArch:      noarch
BuildRequires:  automake

%description
Stout is a header only library that is contains a series of primitives 
to assist in the development of building sturdy C++ applications. Currently this
application is leveraged by Mesos.

%package devel
Summary:        Header files (TBD)
Group:          Development/Libraries
Provides:       %{name}%{?isa} = %{version}-%{release}
Requires:       %{name}%{?isa} = %{version}-%{release}
Requires:       boost-devel
Requires:       protobuf-devel
## TBD - glog removed in the future
Requires:       glog-devel  
Requires:       gmock-devel
Requires:       gtest-devel

%description devel
Headers used for for development of sturdy applications, and leveraged by Mesos.
Note: as that project has only headers (i.e., no library/binary object),
this package (i.e., the -devel package) is the one containing most of the 
project.

%prep
%setup -qn %{name}-%{commit}

%build
./bootstrap
%configure
make %{?_smp_mflags} 

%install
rm -rf %{buildroot}
#installation options don't actually do anything, why even use auto-tools
%make_install
mkdir -p %{buildroot}%{_includedir}/
cp -r ./include/stout %{buildroot}%{_includedir}/

%files devel
%{_includedir}/%{name}/
%doc LICENSE README.md

%changelog
* Mon Jul 29 2013 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.1.0-1.270dba8
- In release added git shotcommit
- In BuildRequires added automake
- Droped BuildRoot target (since Fedora 18 was deprecated)
- Dropped %%clean section (since Fedora 18 was deprecated)
- Dropped %%defattr directives (since Fedora 18 was deprecated)
- Dropped %%files section (not needed)
- other fixes

* Mon Jul 29 2013 Timothy St. Clair <tstclair@redhat.com> 0.1.0-1
- initial fedora package
